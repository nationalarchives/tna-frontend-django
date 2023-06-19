// xidel -se 'request-combine("http://127.0.0.1:8000/piwik.php",{"action_name":"Example",...})/url'
// # curl "http://127.0.0.1:8080/components/card?title=CUSTOM%20TITLE&text=Lorem%20ipsum" > card.txt
// curl "http://127.0.0.1:8080/components/card?title=CUSTOM%20TITLE&text=Lorem%20ipsum"
// # cat /Users/andrew/git/tna-frontend/src/nationalarchives/components/card/fixtures.json
// cat jq .fixtures /Users/andrew/git/tna-frontend/src/nationalarchives/components/card/fixtures.json

import fetch from "node-fetch";
import fs from "fs";
import { diffChars } from "diff";
import { globSync } from "glob";
import { html_beautify } from "js-beautify/js/lib/beautify-html.js";

const fixturesDirectory = `/Users/andrew/git/tna-frontend/src/nationalarchives/components/`;

const components = globSync(`${fixturesDirectory}*/fixtures.json`)
  .map((componentFixtureFile) =>
    componentFixtureFile
      .replace(new RegExp(`^${fixturesDirectory}`), "")
      .replace(new RegExp(/\/fixtures.json$/), "")
  )
  .filter((component) => component === "card");

components.forEach((component) => {
  const { fixtures } = JSON.parse(
    fs.readFileSync(`${fixturesDirectory}${component}/fixtures.json`, "utf8")
  );
  fixtures.forEach(async (fixture) => {
    // console.log(fixture.options)
    // console.log(objectToQuerystring(fixture.options))
    const response = await fetch(
      `http://127.0.0.1:8080/components/${component}?params=${encodeURIComponent(
        fixture.options
      )}`
    );
    const body = await response.text();
    const bodyPretty = html_beautify(body.replace(/(\n\s*){1,}/g, ""));
    const fixturePretty = html_beautify(
      fixture.html.replace(/(\n\s*){1,}/g, "")
    );

    const diff = diffChars(fixturePretty, bodyPretty)
      .map(
        (part) =>
          `${part.added ? "\x1b[32m" : part.removed ? "\x1b[31m" : "\x1b[0m"}${
            part.value
          }`
      )
      .join("");

    const mismatch = bodyPretty !== fixturePretty;
    if (mismatch) {
      console.error(`  🔴 [FAIL] ${fixture.name}\n`);
      const diff = diffChars(fixturePretty, bodyPretty)
        .map(
          (part) =>
            `${
              part.added ? "\x1b[32m" : part.removed ? "\x1b[31m" : "\x1b[0m"
            }${part.value}`
        )
        .join("");
      console.log(diff);
      console.log("\n");
    } else {
      console.log(`  🟢 [PASS] ${fixture.name}`);
    }
  });
});
