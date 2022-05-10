import { expect } from "@playwright/test";
import { injectAxe, getViolations, Options } from "axe-playwright";
import { test } from "@jupyterlab/galata";
import { createHtmlReport } from "axe-html-reporter";
import fs from "fs";
import * as path from "path";

const LORENZ = "Lorenz.ipynb";
const AXE_CONFIG: Options = {
  detailedReport: true,
  detailedReportOptions: { html: true },
  axeOptions: {
    runOnly: {
      type: "tag",
      // all tags and standards listed here:
      // https://www.deque.com/axe/core-documentation/api-documentation/#axe-core-tags
      values: ["wcag2a", "best-practice"],
    },
  },
};

async function axe(page, testInfo) {
  await injectAxe(page);

  const violations = await getViolations(page, null, AXE_CONFIG);
  const axeResultsJsonFilepath = testInfo.outputPath("axe-results.json");
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

// playwright records the browser window while running, and then uploads the
// video with the test results to help with debugging. So here we scroll to the
// bottom of the notebook so that if somebody needs to watch the video, they can
// see the whole notebook from beginning to end.
async function scrollToBottom(page) {
  await page.evaluate(() => {
    for (let i = 0; i < document.body.scrollHeight; i += 100) {
      window.scrollTo(0, i);
    }
  });
}

/**
 * In these tests we use the Axe accessibility testing engine to run analysis on
 * page
 * @see https://github.com/abhinaba-ghosh/axe-playwright
 */
test.describe("jupyterlab accessibility checks", () => {
  test.beforeEach(async ({ page, tmpPath }) => {
    const notebooksDirectory = path.resolve(__dirname, "../notebooks/");
    console.log("notebooks dir", notebooksDirectory);
    await page.contents.uploadDirectory(notebooksDirectory, tmpPath);
  });

  test("notebook a11y LORENZ execute false", async ({
    page,
    tmpPath,
  }, testInfo) => {
    await page.notebook.openByPath(`${tmpPath}/${LORENZ}`);
    await scrollToBottom(page);
    const violations = await axe(page, testInfo);
    await expect(violations).toEqual([]);
  });

  test("notebook a11y LORENZ execute true", async ({
    page,
    tmpPath,
  }, testInfo) => {
    await page.notebook.openByPath(`${tmpPath}/${LORENZ}`);
    await page.notebook.run();
    await scrollToBottom(page);
    const violations = await axe(page, testInfo);
    await expect(violations).toEqual([]);
  });
});
