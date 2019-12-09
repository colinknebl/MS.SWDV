/**
 * Explain what is an error first callback?  Please provide a coded example.
 * - An error first callback is a callback that receives an error as the first parameter. If no error
 *   occurred, the first parameter is null/undefined. The
 */
function takesCallback(
  /** @type {(error: Error, data?: any) => void} */ errorFirstCallback
) {
  try {
    // .. do something here
    errorFirstCallback(null, "data would go here");
  } catch (err) {
    console.error("Uh oh! An error occurred!");
    errorFirstCallback(err);
  }
}

takesCallback(function(error, data) {
  if (error) {
    // the function failed
    return;
  }
  console.log("data", data);
});

/**
 * Explain what Promises are.  Please provide a coded example.
 * - Promises are a way to work with data asynchronously. Using a promise you can attach handlers
 *   that will be run when the Promised in resolved (at some point in the future). The fetch API is
 *   an example of a promise, but promises can also be from scratch.
 */
// example with fetch
fetch("url/goes/here")
  .then(data => {
    console.log("the data returned from the request");
  })
  .catch(err => {
    console.error("Uh oh! An error occurred!");
  });

// example from scratch
const promise = new Promise((resolve, reject) => {
  fetch("url/goes/here")
    .then(data => {
      console.log("the data returned from the request");
      resolve(data);
    })
    .catch(err => {
      console.error("Uh oh! An error occurred!");
      reject(err);
    });
});

promise
  .then(data => {
    console.log("data", data);
  })
  .catch(err => {
    console.error(err);
  });

/**
 * What is a test pyramid?  Please give an example.
 * - A test pyramid is exactly that - an illustration of a pyramid. The pyramid represents
 *   3 different levels of testing. At the base of the pyramid is unit tests. Unit tests test
 *   small pieces of code, typically a single function, and make up the majority of the test
 *   portfolio.
 *
 *   The middle tier of the test pyramid is service/integration tests. This layer of testing
 *   tests how the application integrates with other services. A service could be a database,
 *   the file system, a code library, a REST API, some third party API, etc. There are less
 *   integration tests than there are unit tests.
 *
 *   The top layer of the pyramid is end-to-end tests. These are the most difficult, and often
 *   brittle tests. There are few E2E tests compared to the amount of unit and integrations
 *   tests included in the test portfolio. The E2E tests test complete flows of an application -
 *   from landing on the page and interacting with the user interface, to HTTP requests and
 *   returned data.
 */

// There are many testing frameworks out there, but this is an example of a simple asserting function
function assert(input) {
  return {
    toBe: function(expected) {
      if (input !== expected) {
        throw new Error(`${input} does not match ${expected}`);
      } else {
        console.log("Test Passed");
      }
    }
  };
}

assert(5).toBe(5); // test will pass
assert("foo").toBe("bar"); // test will fail
