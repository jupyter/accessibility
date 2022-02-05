import galataConfig from "@jupyterlab/galata/lib/playwright-config";
import { PlaywrightTestConfig, devices } from "@playwright/test";
// playwright.config.ts
import { expect } from '@playwright/test'
import { matchers } from 'expect-axe-playwright'

expect.extend(matchers)
// modified from https://github.com/MarcusFelling/demo.playwright/blob/main/accessibility/playwright.config.ts
/**
 * See https://playwright.dev/docs/test-configuration.
 */
const config: PlaywrightTestConfig = {
  ...galataConfig,

  testDir: "./test",

  /* Maximum time one test can run for. */
  timeout: 60 * 1000,

  expect: {
    /**
     * Maximum time expect() should wait for the condition to be met.
     * For example in `await expect(locator).toHaveText();`
     */
    timeout: 5000,
  },

  /* Fail the build on CI if you accidentally left test.only in the source code. */
  forbidOnly: !!process.env.CI,

  /* Retry on CI only */
  retries: process.env.CI ? 2 : 0,

  /* Opt out of parallel tests on CI. */
  workers: process.env.CI ? 1 : undefined,

  /* Reporter to use. See https://playwright.dev/docs/test-reporters */
  reporter: "html",

  /* Shared settings for all the projects below. See https://playwright.dev/docs/api/class-testoptions. */
  use: {
    /* Maximum time each action such as `click()` can take. Defaults to 0 (no limit). */
    actionTimeout: 0,

    /* Base URL to use in actions like `await page.goto('/')`. */
    // baseURL: process.env.BASEURL,

    /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
    trace: "on",

    acceptDownloads: true,

    // from RetroLab's playwright.config: https://github.com/jupyterlab/retrolab/blob/main/ui-tests/playwright.config.ts
    appPath: "/retro",

    video: "retain-on-failure",
  },

  /* Configure projects for major browsers */
  projects: [
    {
      name: "chromium",

      /* Project-specific settings. */
      use: {
        ...devices["Desktop Chrome"],
      },
    },

    // {
    //   name: "firefox",
    //   use: {
    //     ...devices["Desktop Firefox"],
    //   },
    // },

    // {
    //   name: "webkit",
    //   use: {
    //     ...devices["Desktop Safari"],
    //   },
    // },
  ],

  webServer: {
    command: "yarn start",
    port: 8888,
    timeout: 120 * 1000,
    reuseExistingServer: !process.env.CI,
  },
};

export default config;
