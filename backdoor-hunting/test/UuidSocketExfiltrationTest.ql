import python
import semmle.code.python.test.Test

from TestPredicate tp
where tp.hasExpectedDiagnostic("Potential UUID exfiltration over a socket – may indicate a tracking or backdoor behavior.")
select tp
