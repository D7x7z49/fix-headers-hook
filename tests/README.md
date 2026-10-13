<!-- @path[tests/README.md] -->
# Common sense for test engineering

write tests that verify necessary conditions only. no test suite covers infinite input space. focus on high-importance inputs and consolidate logic you trust. use monitoring and fast rollback for untested areas.

before writing a test, decide its type by scope.

- unit tests
  - file pattern: `*.unit.test.*`
  - one test per cyclomatic complexity branch
  - no external calls; use in-memory fakes

- component tests
  - file pattern: `*.component.test.*`
  - cover public interface main scenarios
  - also cover critical exceptions

- integration tests
  - file pattern: `*.integration.test.*`
  - test only actually used component combinations
  - mock only at component boundaries

- end-to-end tests
  - file pattern: `*.e2e.test.*`
  - limit to five or fifteen workflows
  - include only workflows with direct business impact

after writing a test, run it with your language's standard test runner. filter by naming patterns via regex or name matching. no specific command is given; adapt to your toolchain.

for external dependencies, mock according to test type.

- unit tests: no external calls
- component tests: stub all external dependencies
- integration tests: mock at boundaries, test real interactions once safe
- E2E tests: use real dependencies in a controlled environment

do not treat coverage as a goal. use coverage only to find uncovered high-importance inputs.

before committing a test, ask yourself five questions.

- without this test, does your confidence in key logic drop?
- on failure, must you fix immediately or can it wait?
- three months later, will you understand why this test exists?
- where would the system break if you delete this test?
- are you testing logic or implementation details?

add UNIX-style comments only for non-obvious assertions or data setup. keep comments short. use prepositions instead of colons or dashes. for example, write "# check for empty list" not "# verify empty list returns zero: edge case".

remember the limitations of this approach. it is not suitable for safety-critical or life-critical systems. rely on monitoring and fast rollback for untested areas.
