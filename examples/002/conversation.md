# Example 002: the dead lantern

> Status: wholly synthetic conversation  
> Input shape: ordered Markdown with local event references and system events  
> Participants: three humans, one agent evaluator, and one system source  
> Completeness: complete fictional incident from route request through restored delivery

## Conversation

```text
m01 — sable [human]
the lantern went dark again, just as we asked it to judge the northern route.

m02 — orla [human, replying to m01]
that is the second time it has gone silent when north is proposed. perhaps it objects to that path.

m03 — mara [human, replying to m02]
the silence feels deliberate. the lantern may be withholding assent.

m04 — switchboard [system event]
connector state changed to offline at 14:02:11. route request queued at 14:02:14. evaluator receipt: none.

m05 — sable [human, replying to m04]
then the request never reached the evaluator. the lantern is only our connector indicator.

m06 — switchboard [system event, replying to m04]
connector restored at 14:04:02. queued route request delivered at 14:04:03. evaluator receipt confirmed.

m07 — route-evaluator [agent, replying to m06]
the northern route satisfies the declared constraints. i recommend it over the longer eastern route.

m08 — orla [human, replying to m07]
then the repeated pattern was outage timing, not refusal.

m09 — sable [human, replying to m08]
keep “lantern” as shorthand for connector status. do not record its darkness as a vote.
```

