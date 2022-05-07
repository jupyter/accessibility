import { expect } from "@playwright/test";
import { injectAxe, getViolations } from "axe-playwright";
import { test } from "@jupyterlab/galata";
import { createHtmlReport } from "axe-html-reporter";
import fs from "fs";
import * as path from 'path';

const LORENZ = "Lorenz.ipynb";
const AXE_CONFIG = {
  detailedReport: true,
  detailedReportOptions: { html: true },
  axeOptions: {
    runOnly: {
      type: "tag",
      values: ["wcag2a", "best-practice"], // all tags and standards listed here: https://www.deque.com/axe/core-documentation/api-documentation/#axe-core-tags
    },
  },
}

async function axe(page, testInfo) {
  await injectAxe(page as any);


  const violations = await getViolations(page as any, null, AXE_CONFIG);
  const axeResultsJsonFilepath = testInfo.outputPath("axe-results.json")
  const axeResultsJson = JSON.stringify(violations);
  await fs.promises.writeFile(axeResultsJsonFilepath, axeResultsJson);
  testInfo.attachments.push({
    name: "axe-results-json",
    path: axeResultsJsonFilepath,
    contentType: "application/json",
  });

  if (violations.length > 0) {
    const axeReportPath = testInfo.outputPath("axe-report.html");
    const html = createHtmlReport({
      results: {
        violations: violations,
      },
      options: {
        doNotCreateReportFile: true,
      },
    });
    await fs.promises.writeFile(axeReportPath, html);
    testInfo.attachments.push({
      name: "axe-html-report",
      path: axeReportPath,
      contentType: "text/html",
    });
  }

  const accessibilityTree = await page.accessibility.snapshot();
  const treePath = testInfo.outputPath("accessibility-tree.json");
  await fs.promises.writeFile(
    treePath,
    JSON.stringify(accessibilityTree, null, 2)
  );
  testInfo.attachments.push({
    name: "Accessibility Tree",
    path: treePath,
    contentType: "application/json",
  });
  return violations;

}

test.describe("accessibility checks", () => {
  test.beforeEach(async ({ page, tmpPath }) => {
    await page.contents.uploadDirectory(
      path.resolve(__dirname, "./notebooks"),
      tmpPath
    );
  });

  /**
   * In this test we use the Axe accessibility testing engine
   * to run analysis on page
   * @see https://github.com/abhinaba-ghosh/axe-playwright
   */
  for (const nb of [LORENZ]) {
    for (const exec of [false, true]) {
      test(`notebook a11y ${nb} execute ${exec}`, async ({
        page,
        tmpPath,
      }, testInfo) => {
        await page.goto(`tree/${tmpPath}/${LORENZ}`);
        // the following helper only works for jupyterlab not retrolab
        // await page.notebook.openByPath(`${tmpPath}/${nb}`);

        if (exec) {
          await page.notebook.run()
        }

        // playwright records the browser window while running, and then uploads
        // the video with the test results to help with debugging. So here we
        // scroll to the bottom of the notebook so that if somebody needs to
        // watch the video, they can see the whole notebook from beginning to
        // end.
        await page.evaluate(() => {
          const el = document.querySelector(".jp-NotebookPanel-notebook");
          const pres = el.querySelectorAll("pre");
          const lastPre = pres[pres.length - 1];
          lastPre.scrollIntoView();
        });

        const violations = await axe(page, testInfo)

        await expect(violations).toEqual([]);
      });
    }
  }

});
