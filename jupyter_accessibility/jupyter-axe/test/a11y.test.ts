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
        await page.notebook.openByPath(`${tmpPath}/${nb}`);

        if (exec) {
          await page.notebook.runCellByCell({})
        }
        const violations = await axe(page, testInfo)

        // await expect(violations).toEqual([]);
      });
    }
  }

});