Note that due to elements of code in this essay it is reproduced in PRE format.

<pre>A Completely Formal Nomic

Submitted in partial fulfilment of the
requirements for the degree of Bachelor
of Nomic.  This Thesis is associated with
the recent Proposal "A B.N. for favor".

Player Favor, Agora Nomic

Introduction

Historically, many of the scams and CFJs in Agora Nomic
have hinged on matters of word-meaning.  Everyday language
is notoriously ambiguous and dependant on assumptions
about speaker and listener intent that are not logically
well-founded; they require the application of what is
often called "common sense" (a loose and imperfectly-shared
collecion of default assumptions, word-usage rules, and so on).

The Rules and Customs of Agora Nomic have historically
had an ambivalent attitude towards common sense.  Judges
have sometimes been allowed or required to exercise it
when the Rules are not clear.  Some Players have cited the
imperfect consensus on matters of common sense in borderline
cases, and tried to reduce or eliminate the Rules' dependence
on it.

CFJs and scams based on word usage are welcomed and relished
by some Players, and despised by others.  Some have accused
the community of making scams impossible by encouraging
Judges to block them by quibbles on word meaning; others
have claimed that without such quibbles, most scams would
be impossible in the first place.

It would be illuminating to consider what a Nomic game
might be like that was wholely lacking in disputes and
disagreements about word usage and meaning, or about
common sense or other broad subjective notions.  Such
a game would be interesting by virtue of the contrasting
light it would throw on Agora and similar Nomics, as well
as potentially leading to interesting games in its own right.

So

The idea is to design a completely formal Game, one in which
there are no rules that have subjective components, or are
otherwise open to disputes about common sense or the
meanings of words.  The game should also be as Nomic-like
as possible, given that restriction, in that the rules of
the game should be represented within, and changeable by
moves of, the game.

This will *not* be "real" Nomic unless we are wildly more
successful than I think we will be.  Because we have to
choose a comparatively simple formal framework (in order
to keep it comprehensible), it's unlikely that we'll
be able to get as "meta" as non-formal Nomic can get.
It will also, of course, not have the fun of Judgement
and dispute about word meanings and intent and sense
and reference and all that that most Nomics offer.  This
is intended to be a *different* game, albeit somewhat
inspired by the usual Nomic.  But there's no claim that it's
better than any other Nomic, or truer to any particular ideal,
or anything like that.

There will, of course, have to be an interface between
the formal system in which the rules sit and the players,
who are out in the physical world.  This interface will be
referred to as the Mechanics of the game, and these will
be subject to all sorts of disputes and things.  But they
are *not* part of the game itself; any issues that come up
about the Mechanics ("I didn't make that move; someone must
have forged the e-mail!") will be extra-game issues, and
will not be expressed or resolved in the gamestate.

Similarly, the language in which the game is expressed will
be subject to change (and in particular to expansion) as
the game goes on, but this again is an extra-game process.
As new verbs or conditions or whatever are added to the
language, we will just have discovered new parts of the
formal space that the game is exploring.  The status of
the language of the game is not contained in the game
itself.  This is another limitation that nonformal Nomic
does not, at least in theory, suffer from.  I suspect,
however, that a strong case could be made for the claim
that any nonformal Nomic played by humans will in fact
be subject to the same sort of limitation, in that humans,
being finite entities instantiated in a limited universe,
cannot ultimately escape all bounds of language themselves.

Relationship to Agora Nomic

Formal Nomic can serve Agora Nomic as a thought-pump, if
nothing else.  If some actual or contemplated feature of
Agora Nomic would be especially hard or easy to add to
a hypothetical game of Formal Nomic, or would require
diddling with the Mechanics, that says something about
the nature of the feature.  If two apparently-similar
ways of embodying within Agora the same basic idea turn
out to have very different implications for a hypothetical
game of Formal Nomic, that says something about the
differences between them.

Formal Nomic might also be a useful, or instructive,
or amusing subgame (probably a Contest) within Agora
Nomic.  One Player would implement (either automatically,
or by hand) the Mechanics, and choose an Initial Set;
the other Players in the jurisdiction of the subgame
would submit input to the Mechanics, changing the state
of the subgame.  Winning the subgame could mean being
awarded the subgame's Treasury, or whatever.

Details / Examples

The rest of this paper consists of a worked-out example
of one completely formal Nomic, including a description
of the mechanics, and an Inital Set (that is, an initial
object-pool).  It is of course only one example; the
basic objective could be accomplished in many other
ways.  For instance, if all the Players were willing
to be computer programmers, the ruleset and gamestate
could be expressed directly as computer program texts
and variable values, at a considerable increase in power,
and a considerable cost in difficulty of play.

For this example, the incoming interface is relatively
simple: when a piece of mail comes in for the "server",
it's parsed into one or more objects in the system.
Each object has a Type of "move", a Sender and Timestamp
filled in from the envelope, a randomly-generated BatchNumber
that's the same for all the objects created by the same piece
of mail, and other fields filled in from the body of the
message.  For instance, a request to register might look like:

   From: Matt Zimola <zimola@peeble.net>
   Date: 14 Aug 1995, 12:36:13 UTC
   Subject: to the Mech server

   REGISTER MattZ

and the corresponding object that gets created might be:

   objectId: 127
   batchId: 114
   moveTimeStamp: 1995/08/14 12:36:13
   moveSender: zimola@peeble.net
   type: move
   subtype: register
   nickname: MattZ

"REGISTER MattZ" is syntactic sugar, to make a common operation
easier.  In its full generality, the incoming Mechanics would
allow the sender of the mail to specify any attributes and values
e wants to (except type, objectId, batchId, and so on).

On the other end, there will be a small set of verbs that
cause extra-game side-effects; primarily mail-sending to let the
physical-world players know what's going on.  But these side-effects
are not defined in or modifiable by the game rules; they are
the Mechanics, not the Rules.  From the point of view of the
game-state itself, the sendFoo() verbs will be no-ops.

A rule is just another object, with Type "rule", an "if"
attribute which is some boolean function of the gamestate,
and a "then" attribute which is some sequence of verbs.
It also has a ruleOrder, to determine which rules get to
look at the game-state first, and probably various other
housekeeping numbers.  (More generally, we can have a
special engineSettings object which would tell the engine
which type of objects are really rules; that would normally
be set to "rule", but could be diddled with for various
special effects.)

The sequence of events in the game is as follows.  Note that
this is again a thing that isn't part of, or changable by,
the Rules, and this is another un-Nomic-like limitation.
It may be possible to make some or all of this stuff adjustable
within the game also, with some effort.  (Note that that effort
would have to be done outside the game, in the Mechanics, to
enable laters efforts within the game.)

  - Something happens: either a new object arrives from the
    physical world via the incoming interface, or a rule
    suddenly fires due to a schedule pop.

  - For each object of Type "rule" in the gamestate, in order
    of ruleOrder, the value of the "if" attribute is
    evaluated.  If the result if "false", we proceed to the
    next "rule" object.  If the result is "true", the verbs in the
    "then" attribute fire, creating or deleting or modifying or
    scheduling objects; then we restart this "for" loop, back at
    the rule with the highest (lowest-numbered) PrecendenceNumber.
    (If a rule fires, but the "then" clause does *not* change
    the game-state, we don't restart.)

  - Once the highest-ruleOrder rule has had its "if" part
    evaluate to "false", we go to sleep again until the next
    thing happens.

There are all sorts of "programming" issues involved in making these
things actually work.  When a rule fires and changes the game-state,
for instance, it will almost always have to make sure that the change
it makes is such that it won't fire again for the same reasons, since
its change will cause a restart, and if no rule with a lower ruleOrder
fires, it will see the game-state again just the way it left it.  So
for instance a rule that gives a player a point because of some
condition should make sure to also make the condition false, otherwise
it may give the player an infinite number of points, one at a time!
(Another aspect of the Mechanics will presumably be an extra-Game
meta-rule like "if the game-state goes into a verifiable loop,
the last player to submit a move wins".)

One way to manage this is to have a rule simply delete the object
that caused it to fire; this is sensible in some cases, although it
will often be better to simply mark it in some way (set the
processedByRule47 attribute to T, for instance), rather than deleting
it, so that other rules with higher ruleOrders will get a chance
to act on it as well.

Below is a sample Initial State.  It includes registration (but not
deregistration or On Hold), proposals (which may contain multiple
Rule Changes), voting (but not multiple votes, or changing votes),
quorum, simple majority (AIs and MIs are quite doable, but are not
in this Initial State), points for voting and having your proposals
pass, and a simple Win on points (which ends the game).  Kudos,
degrees, Win Tokens, Extra Votes, the Potato, and some other familiar
Agora concepts would fit into this set in reasonably simple ways.

Some other concepts are much harder; for instance, the idea
of sub-rulesets that only apply to some Players, as in Group
Ordinances and Contest Regulations.  Platonic sub-rules are
especially hard to formalize.  For instance, if a Group
Ordinance says that in some circumstances a Group Member
shall transfer fifteen Marks to a non-Member, that's
acceptable.  If it says the opposite, that some non-Member
shall transfer fifteen Marks to some Member, that isn't.
In both cases, both a Member and non-Member appear in the
subrule; formalizing the difference between the two is a
subject for further study.

I haven't actually *implemented* any of this as a computer program,
and I'm not sure that I have any interest in doing so.  But I hope
it will spur some interesting discussion nonetheless...

A note on scams: an amusing proof that scams are entirely
possible in this formal Nomic.  In the first draft of this Initial
State, Rule 16 didn't set the "cleanup" attribute of incoming votes
to F.  So if you submitted a vote, and set "cleanup" to T in the
move object, you'd get your point for voting, but the vote would
be destroyed by the Sweeper, so you could do it again.  And again.
And again.  Getting a point each time, and winning at will.  Easy
to fix, but illustrative!  (In the very first version of Rule 16,
it didn't even have the check to ensure that the proposal ID was
valid, making it easy to win by voting for a hundred non-existent
proposals.)

Anyway:

Basic attributes of objects:
  objectId - a number, used as a handle for talking
     about an object, assigned sequentially by the system
     when the object is created.  Match clauses always
     find the matching object with the lowest objectId.
  type - tells what it is; the incoming interface produces only
     objects of type "move".  The rule engine gets its settings
     from the first objects of type "engineControls", and
     runs only objects whose type is the same as the runType
     attribute of engineControls. All other types have meaning only to
     rules.  A basic type in the initial set is "player".

Move attributes set by the incoming interface (these attributes
are always assigned; any and all other attributes besides Type
can be set by the incoming mail explicitly):
  moveSender - user@host.domain that sent the mail
  moveTimeStamp - yyyymmddhhmmss (a time-format string), from
     the date: line of the mail
  moveBatch - a contentless id assigned to all the "move"
     objects that come in in the same piece of mail (for
     batching up multiple Rule Changes into a single proposal,
     etc)
Except for these three, and type (which is always "move"), the
sender of the mail can control all the attributes of the move object.
Syntactic sugar of various kinds will presumably be provided for
common cases.

Rule attributes used by the engine:
  ruleOrder - rules are run in order of ruleOrder, lowest to highest.
  if - condition tested when a rule is run.
  then - verbs executed when an if is true; if this causes any
     change to the existing objects (creation, deletion,
     amendment), the ruleset is restarted.

Some verbs:
  delete(match) - deletes the matching object (with the lowest
     objectId, as usual)
  create(match) - creates a matching object
  set(match1)(match2) - Changes the object matching match1 so
     that it matches match2.
  send(userid@host.domain[....])(expression) - queues up the value
     of the expression for sending to userid@host.domain (or list thereof).
  sendObject(userid@host.domain[...])(match)(string) - queues up a
     print form of the matching object, with the string for a
     header, for sending.
  sendNow() - actually sends all queued stuff off.

Some functions for use in expressions:
  exists(match)
  count(match)
  timeGE(timevalue) - Tests if the current time is >= the given
     time.  Used for timers.  A possible engine optimization:
     duing each pass, keep track of the lowest-value timeGE
     that fails; set an actual timer to re-check all rules
     at that time, if nothing else has happened in the meantime.

Notes:
  - Some sort of "for" clause in rules may be needed for performance
    and clarity reasons.  Otherwise, the only way to do something
    like sending the entire ruleset to a player in response to a
    query move would be to do <number of="" rules="">passes through the
    first part of the ruleset, using some kludged-up bookkeeping
    attribute or object to keep track of which rules we haven't
    sent yet.  Maybe that's OK?
  - Perhaps allow a rule to say that the engine *shouldn't* restart
    the ruleset after processing it?  That, instead, it should just
    test the rule itself again, and then proceed onwards?
  - A more radical change to this model would be to have all
    object-changes take place in a second, "shadow", copy of
    the object-pool, and switch over to that object-pool only
    when no rule in the current pool wants to make any changes.
    Could be an engineControls switch?
  - Probably be good to have a setall(match1)(match2), that would
    efficiently set all objects matching match1 to match match2.

An Intial State
---------------

Loose conventions about ruleOrder:

  We will use ruleOrder 10000-19999 for rules that don't delete
  the object that sets them off (although they may set some
  attributes so that it doesn't set them off again).

  We will use ruleOrder 30000-39999 for rules that do delete, or
  otherwise make very significant changes (like changes of type)
  to the object that sets them off.

  We will use ruleOrder 99000-99999 for rules that should basically
  only run for cleanup-type reasons at the very end of an event.

Initial engine settings and (empty) player-list:

  objectId: 1
  type: engineSettings
  runType: rule

  objectId: 2
  type: playerList
  listContents: ""

Rules about registration:

 objectId: 3
 ruleOrder: 30010
 type: rule
 if: exists(type=="move" & subtype=="register" & moveSender==%s &
            nickname!="" & nickname==%n & moveTimeStamp==%tm & objectId==%mo) &
     !exists(type=="player" & nickname==%n) &
     exists(type=="playerList" & listContent==%pl)
 then: create(type=="player" & defaultEmail==%s & nickname==%n &
              registeredAt==%tm & score==0 & objectId==%po) &
       set(objectId==%mo)(processed==T & cleanup==T) &
       create(type=="newPlayer" & reference==%po & cleanup==T) &
       send(%pl,"New player" %n "registered at" %tm) &
       send(%s,"Welcome to Engine City," %n"!")
 comment: "if someone's registering, and e gave a nickname that
           isn't already in use, create a proxy object for em with
           their information, note that the move was processed for
           later cleanup, and create a newPlayer object for other
           rules to process.  Also tell everyone."

 objectId: 4
 ruleOrder: 30020
 type: rule
 if: exists(type=="move" & subtype=="register" & processed!=T &
            moveSender==%s & nickname!="" & nickname==%n & objectId==%mo) &
     exists(type=="player" & nickname==%n)
 then: sendObject(%s)(objectId==%mo)("A player" %n "is already registered") &
       delete(objectId==%mo)
 comment: "handle error case where someone tries to register with a
           name that's already in use."

 objectId: 5
 ruleOrder: 30030
 type: rule
 if: exists(type=="move" & subtype=="register" & moveSender==%s &
            nickname=="" & objectId==%mo) &
 then: sendObject(%s)(objectId==%mo)("You have to give a nickname when you
       register") & delete(objectId==%mo)
 comment: "handle error case where someone tries to register without
           a name."

 objectId: 6
 ruleOrder: 30040
 type: rule
 if: exists(type=="move" & from=="" & moveSender==%s & objectId==%o) &
     exists(type=="player" & defaultEmail==%s & nickname==%n)
 then: set(objectId==%o)(from==%n)
 comment: "if no from is given on a move, guess from the email address"

 objectId: 7
 ruleOrder: 30050
 type: rule
 if: exists(type=="move" & from==%f & moveSender==%s & objectId==%mo) &
     !exists(type=="player" & nickname==%f)
 then: sendObject(%s)(objectId==%mo)("You are no known player.") &
       delete(objectId==%mo)

 objectId: 8
 ruleOrder: 30060
 type: rule
 if: exists(type=="newPlayer" & listed!=T & defaultEmail==%e &
            objectId==%po) &
     exists(type=="playerList" & listContent==%l & objectId==%lo)
 then: set(objectId==%po)(listed==T) &
       set(objectId==%lo)(listContent==%l %e)
 comment: "Maintain a list of all player email addresses, for
           mass sendings"

A simple Win rule:

  objectId: 9
  ruleOrder: 10010
  type: rule
  if: exists(type=="player" & score>100 & nickname==%n & objectId==%o) &
      !exists(type=="win" & who==%o) &
      exists(type=="playerList" & listContent==%pl)
  then: create(type=="win" & who==%o) &
        send(%pl,%n "wins the game!")
  comment: "if a player has over 100 points, e wins"

  objectId: 10
  ruleOrder: 10020
  type: rule
  if: exists(type=="win")
  then: halt()
  comment: "the game ends when one or more players win"

Rules about Proposing:

  objectId: 11
  ruleOrder: 30120
  type: rule
  if: exists(type=="move" & subtype=="ruleChange" &
            ruleChangeType=="repeal" & target==%t &
            batchid==%b & objectId==%mo) &
      exists(objectId==%to & type=="rule")
  then: set(objectId==%mo)(type="changeBeingVotedOn")
  comment: "snarf in an incoming repeal rule change; we'll
     let ones that attempt to repeal a non-existing rule just
     fall through to the general error handler at first."

  objectId: 12
  ruleOrder: 30130
  type: rule
  if: exists(type=="move" & subtype=="ruleChange" &
            ruleChangeType=="amend" & target==%t &
            batchid==%b & objectId==%mo) &
      exists(objectId==%to & type=="rule")
  then: set(objectId==%mo)(type="changeBeingVotedOn")
  comment: "snarf in an incoming amendment rule change"

  objectId: 13
  ruleOrder: 30140
  type: rule
  if: exists(type=="move" & subtype=="ruleChange" &
            ruleChangeType=="create" & target==%t &
            batchid==%b & objectId==%mo)
  then: set(objectId==%mo)(type="changeBeingVotedOn")
  comment: "snarf in an incoming create rule change"

  objectId: 14
  ruleOrder: 30150
  type: rule
  if: exists(type=="changeBeingVotedOn" & sent!=T & batchId==%b &
            objectId==%o) &
      exists(type=="playerList" & listContent==%pl)
  then: sendObject(%pl,%o,"Proposed rule-change (proposal" %b"):") &
        set(objectId==%o)(sent==T)
  comment: "Tell all players about new proposals"

  objectId: 15
  ruleOrder: 30160
  type: rule
  if: exists(type="changeBeingVotedOn" & batchid==%b) &
      !exists(type=="voteInProgress" & propId==%b)
  then: create(type=="voteInProgress" & propId==%b) &
        expiryTime==timeNow()+10*24*60*60)
  comment: "Creates the voting object representing a pending Proposal"

Rules about Voting:

  objectId: 16
  ruleOrder: 30220
  type: rule
  if: exists(type=="move" & subtype=="vote" & propID==%p &
        from==%f & objectId==%o) &
      exists(type=="player" & nickname==%f) &
      exists(type="voteInProgress" & propId==%b) &
      !exists(type=="vote" & propID==%p & from==%f)
  then: set(objectId==%o)(type=="vote" & credited==F & cleanup==F)
  comment: "One Player, one unchangable vote per proposal"

  objectId: 17
  ruleOrder: 30230
  type: rule
  if: exists(type=="vote" & from==%f & credited==F & objectId==%vo) &
      exists(type=="player" & nickname==%f & score==%s & objectId==%po)
  then: set(objectId==%po)(score==1+%s) &
        set(objectId==%vo)(credited==T)
  comment: "One Point when you vote"

The End of the Voting Period:

  objectId: 18
  ruleOrder: 30320
  type: rule
  if: exists(type=="voteInProgress" & timeGE(expiryTime) &
        objectId==%o)
  then: set(%o)(type="voteCompleted")

  objectId: 19
  ruleOrder: 30330
  type: rule
  if: exists(type=="voteCompleted" & propId==%p) &
      exists(type=="vote" & propId==%p & from==%f & vote==%vc &
            noted!=T & objectId==%vo) &
      exists(type=="playerList" & listContent==%pl)
  then: set(objectId==%vo)(noted==T) &
        send(%pl,"Player" %f "receives one point for voting" %vc "on" %p)
  comment: "Announce content of votes"

Tallying Votes:

  objectId: 20
  ruleOrder: 30420
  type: rule
  if: exists(type=="voteCompleted" & objectId==%o & propId==%p &
            objectId==%o) &
      count(type=="vote" & propId==%p)<(count(type=="player")/4) &
      exists(type=="playerList" & listContent==%pl)
  then: set(objectId==%o)(type="proposalFailed" & cleanup==T) &
        send(%pl,"Proposal" %p "fails quorum.")

  objectId: 21
  ruleOrder: 30430
  type: rule
  if: exists(type=="voteCompleted" & objectId==%o & propId==%p &
            objectId==%o) &
      count(type=="vote" & propId==%p & vote=="FOR")>
      count(type=="vote" & propId==%p & vote=="AGAINST") &
      exists(type=="playerList" & listContent==%pl)
  then: set(objectId==%o)(type="proposalPassed" & credited==F) &
        send(%pl,"Proposal" %p "passes.")

  objectId: 22
  ruleOrder: 30440
  type: rule
  if: exists(type=="voteCompleted" & objectId==%o & propId==%p &
            objectId==%o) &
      count(type=="vote" & propId==%p & vote=="FOR")<=
      count(type=="vote" & propId==%p & vote=="AGAINST") &
      exists(type=="playerList" & listContent==%pl)
  then: set(objectId==%o)(type="proposalFailed" & cleanup==T) &
        send(%pl,"Proposal" %p "fails.")

  objectId: 23
  ruleOrder: 30450
  type: rule
  if: exists(type="proposalPassed" & from==%f & credited==F &
            objectId==%pro) &
      exists(type=="player" & nickname==%f & score==%s & objectId==%plo) &
      exists(type=="playerList" & listContent==%pl)
  then: set(objectId==%pro)(credited==T) &
        set(objectId==%plo)(score==5+%s) &
        send(%pl,%f "receives 5 points for the proposal ("5+%s")")
  comment: "Five points when your proposal passes."

Implementing passed rulechanges:

  objectId: 24
  ruleOrder: 30520
  type: rule
  if: exists(type="proposalPasssed" & propId==%b) &
      exists(type="changeBeingVotedOn" & batchId==%b & objectId==%o)
  then: set(objectId==%o)(type=="changePassed")

  objectId: 25
  ruleOrder: 30530
  type: rule
  if: exists(type=="changePassed" & ruleChangeType=="repeal" &
            target==%t & objectId==%o)
  then: delete(objectId==%t) &
        set(%o)(type=="changeDone" & cleanup==T)

  objectId: 26
  ruleOrder: 30540
  type: rule
  if: exists(type=="changePassed" & ruleChangeType=="amend" &
            target==%t & newif==%ni & newthen==%nt & neworder==%no &
            objectId==%o)
  then: set(objectId==%o)(if==%ni & then==%nt & ruleOrder==&no) &
        set(%o)(type=="changeDone" & cleanup==T)

  objectId: 27
  ruleOrder: 30550
  type: rule
  if: exists(type=="changePassed" & ruleChangeType=="create" &
            newif==%ni & newthen==%nt & neworder==%no &
            objectId==%o)
  then: create(type=="rule" & if==%ni & then==%nt & ruleOrder==&no) &
        set(%o)(type=="changeDone" & cleanup==T)

Cleanup Rules:

 objectId: 28
 ruleOrder: 99910
 type: rule
 if: exists(type=="proposalFailed" & propId==%p) &
     exists(type=="changeBeingVotedOn" & batchId==%p & objectId==%o)
 then: delete(objectId==%o)

 objectId: 29
 ruleOrder: 99920
 type: rule
 if: exists(type=="proposalFailed" & propId==%p) &
     exists(type=="vote" & batchId==%p & objectId==%o)
 then: delete(objecId==%o)

 objectId: 30
 ruleOrder: 99930
 type: rule
 if: exists(type=="proposalPassed" & propId==%p) &
     exists(type=="vote" & batchId==%p & objectId==%o)
 then: delete(objectId==%o)

 objectId: 31
 ruleOrder: 99940
 type: rule
 if: exists(type=="move" & processed!=T & objectId==%o &
            moveSender==%ms)
 then: sendObject(%ms)(objectId==%o)("This move didn't do anything") &
       delete(objectId==%o)
 comment: "If an unprocessed move is hanging around, delete it,
           and send a warning to the sender."

 objectId: 32
 ruleOrder: 99980
 type: rule
 if: exists(cleanup==T & objectId==%o)
 then: delete(objectId==%o)
 comment: "the Final Sweeper"

 objectId: 33
 ruleOrder: 99990
 type: rule
 if: T
 then: sendNow()
 comment: "Send out accumulated mailings"</number> </zimola@peeble.net></pre>