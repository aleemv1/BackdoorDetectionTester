/**
 * @name UUID Socket Exfiltration
 * @description Detects functions that exfiltrate UUIDs over sockets.
 * @kind problem
 * @problem.severity warning
 * @id python/uuid-socket-exfiltration
 */

import python

from FunctionCall call
where call.getTarget().getName() = "send" and
      call.getAnArgument().toString().matches("%uuid.uuid4%")
select call, "Potential UUID exfiltration over a socket – may indicate a tracking or backdoor behavior."
