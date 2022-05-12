import { expect } from "@playwright/test";
import { test } from "@jupyterlab/galata";
import * as path from "path";

const notebooksDirectory = path.resolve(__dirname, "../../notebooks/");
// Lorenz notebook file name
const LORENZ = "Lorenz.ipynb";

// playwright records the browser window while running, and then uploads the
// video with the test results to help with debugging. So here we scroll to the
// bottom of the notebook so that if somebody needs to watch the video, they can
// see the whole notebook from beginning to end.
async function scrollNotebookToBottom(page) {
  await page.evaluate(() => {
    const notebookEl = document.querySelector(".jp-Notebook");
    const scrollableHeight = notebookEl.scrollHeight - notebookEl.clientHeight;
    for (let i = 0; Math.abs(scrollableHeight - i) < 1; i += 1) {
      notebookEl.scrollTo(0, i);
    }
  });
}

/**
 * In these tests we use the Axe accessibility testing engine to run analysis on
 * page
 * @see https://github.com/abhinaba-ghosh/axe-playwright
 */
test.describe("JupyterLab accessibility checks", () => {
  test.beforeEach(async ({ page, tmpPath }) => {
    await page.contents.uploadDirectory(notebooksDirectory, tmpPath);
  });

  test("Lorenz notebook before running all cells", async ({
    page,
    tmpPath,
  }) => {
    await page.notebook.openByPath(`${tmpPath}/${LORENZ}`);
    await scrollNotebookToBottom(page);
    await expect(page).toBeAccessible();
  });

  test("Lorenz notebook after running all cells", async ({
    page,
    tmpPath,
  }) => {
    await page.notebook.openByPath(`${tmpPath}/${LORENZ}`);
    await page.notebook.run();
    await scrollNotebookToBottom(page);
    await expect(page).toBeAccessible();
  });
});
