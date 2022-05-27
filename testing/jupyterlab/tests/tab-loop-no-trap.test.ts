/**
 * This test checks whether a user, starting from the top and only pressing the
 * tab key, can tab through the entire app and return to where they started.
 *
 * This means that a first-level tab-through of the app encounters no keyboard
 * traps.
 */

import { expect } from "@playwright/test";
import { test } from "@jupyterlab/galata";

test.describe("when pressing tab key repeatedly", () => {
  test("should cycle through elements back to the start", async ({ page }) => {
    await page.keyboard.press("Tab");
    // The first element we tab to will be used as reference point of
    // comparison.
    const firstElementTabbedTo = await page.evaluateHandle(
      "document.activeElement"
    );
    let encounteredFirstElementAgain = false;
    let encounteredOtherElement = false;
    // i < 100 is arbitrary; however, this test should certainly fail if the
    // user has to tab more 100 times to return to the top.
    for (let i = 0; i < 100; i++) {
      await page.keyboard.press("Tab");
      const sameActiveElement = (el) => el === document.activeElement;
      // Is the element that we are currently tabbed on the same as the first
      // element that we tabbed to earlier?
      const currentIsFirst = await page.evaluate(
        sameActiveElement,
        firstElementTabbedTo
      );
      if (currentIsFirst) {
        encounteredFirstElementAgain = true;
      } else {
        // If we do not check whether the user encounters another element while
        // tabbing, then the test would pass even if the first element they
        // tabbed to was a tab trap.
        encounteredOtherElement = true;
      }
      if (encounteredFirstElementAgain) {
        firstElementTabbedTo.dispose();
        break;
      }
    }
    expect(
      encounteredFirstElementAgain,
      "should have cycled back to first element"
    ).toBe(true);
    expect(
      encounteredOtherElement,
      "should have tabbed through at least one other element"
    ).toBe(true);
  });
});
