import { expect } from "@playwright/test";
import { injectAxe, getViolations } from "axe-playwright";
import { test } from "./fixtures";
import { createHtmlReport } from "axe-html-reporter";
import fs from "fs";

const LORENZ = "Lorenz.ipynb";

test.describe.parallel("accessibility checks", () => {
  test.beforeEach(async ({ page, tmpPath }) => {
    await page.contents.uploadFile(
      __dirname + "/" + LORENZ,
      `${tmpPath}/${LORENZ}`
    );
  });

  /**
   * In this test we use the Axe accessibility testing engine
   * to run analysis on page
   * @see https://github.com/abhinaba-ghosh/axe-playwright
   */
  test("Check Lorenz notebook accessibility before running all cells", async ({
    page,
    tmpPath,
  }, testInfo) => {
    await page.goto(`notebooks/${tmpPath}/${LORENZ}`);

    // inject the axe-core runtime into the page under test
    await injectAxe(page as any);

    const violations = await getViolations(page as any, null, {
      detailedReport: true,
      detailedReportOptions: { html: true },
      axeOptions: {
        runOnly: {
          type: "tag",
          values: ["wcag2a", "best-practice"], // all tags and standards listed here: https://www.deque.com/axe/core-documentation/api-documentation/#axe-core-tags
        },
      },
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

    await expect(violations).toEqual([]);
  });

  test("Check Lorenz notebook accessibility after running all cells", async ({
    page,
    tmpPath,
  }, testInfo) => {
    await page.goto(`notebooks/${tmpPath}/${LORENZ}`);

    await page.click('.lm-MenuBar-itemLabel:has-text("Run")');
    await page.click('.lm-Menu-itemLabel:has-text("Run All Cells")');
    await page.waitForSelector('pre:has-text("Okay all done running 4")');
    await page.evaluate(() => {
      const el = document.querySelector(".jp-NotebookPanel-notebook");
      const pres = el.querySelectorAll("pre");
      const lastPre = pres[pres.length - 1];
      lastPre.scrollIntoView();
    });

    // inject the axe-core runtime into the page under test
    await injectAxe(page as any);

    const violations = await getViolations(page as any, null, {
      detailedReport: true,
      detailedReportOptions: { html: true },
      axeOptions: {
        runOnly: {
          type: "tag",
          values: ["wcag2a", "best-practice"], // all tags and standards listed here: https://www.deque.com/axe/core-documentation/api-documentation/#axe-core-tags
        },
      },
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

    await expect(violations).toEqual([]);
  });
});
