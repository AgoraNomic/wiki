**A case of problematic precedence**

Submitted Wed, 13 Nov 1996 20:30, for Associate of Nomic, by Andre.

In this thesis I will present a paradox in the precedence rules for a Nomic game. One example of these is of course known to us all: Suppose the following rules would exist:

> 4000 The Virus is green. This rule takes precedence over rule 4010.

> 4010 The Virus is blue. This rule takes precedence over rule 4011.

> 4011 The Virus is yellow. This rule takes precedence over rule 4000.

What colour would the Virus have? Rule 4000 takes precedence over 4010, 4010 over 4011 and 4011 over 4000\. So all have another rule of higher precedence conflicting with it. It's a problem that is known in real-life situations as well: If three vehicles come to a crossing, situations can occur in which each has to let one of the other two go first. This, however, is only an omission in the precedence rules. It could even be argued that our Rule 1030 has already overcome it, although in my opinion it does not (although it does alleviate some other precedence problems).

This is not the point I want to discuss here. My example is in a way more disturbing, because no change in the precedence rules will effectively correct it.

Suppose a rule would be enacted, with MI=1, and the following text:

> Rule 9999/0

> Andre may not deregister.

Will it have effect? Of course not. It is in conflict with Rule 113, which has higher precedence. New try:

> Rule 9999/1

> Andre may not deregister. This Rule takes precedence over Rule 113.

Again Rule 9999 and Rule 113 are in conflict. Let's look at the precedence Rules. Rule 1482 says:

> In a conflict between Rules with different Mutability Indices, the Rule with the higher Mutability Index takes precedence over the Rule with the lower Mutability Index. [[<font color="#0000FF">1</font>](#ref1)]

So, at first sight this would be no problem: Rule 1482 specifies that Rule 113 still takes precedence. There is more here than meets the eye, though. Rule 9999 says it takes precedence over Rule 113\. Rule 1482 says Rule 113 takes precedence over Rule 9999\. So, in fact there is a conflict between Rule 1482 and Rule 113\. This Rule is of course solved by looking which of the two Rules takes precedence. This is Rule 1482, so in fact Rule 113 takes precedence over Rule 9999\. However, this leads to the following, paradox causing Rule:

> Rule 9999/2

> Andre may not deregister. This Rule takes precedence over Rule 113 and Rule 1482.

Again Rule 9999 and Rule 113 are in conflict. Rule 9999 and 1482 are in conflict, but this time - Who wins this conflict? Both claim to be the winner, and who is to arbitrate? The Rules can't tell you.

As with so many paradoxes this paradox revolts around self-reference. In Nomic we already have the Paradox of Self-amendment, which in fact kind of started the whole game, which appears when the rule changing rules are changed [[<font color="#0000FF">2</font>](#ref2)], and the pardoxes that occur when a CFJ has to regulate its own legality or application. Here it is the precedence between precedence rules that causes the problem.

What can we do about this? As will be clear from the preceding discussion, adding or changing precedence Rules will not solve the problem, and can even deteriorate it. Two ways are still open:

Add a meta-rule (does anyone have a quasi-official set of them?) to this effect, for example: If two Rules regulating precedence conflict on the subject which of them takes precedence, then the oldest one does.

Disallow the creation of this kind of disturbing Rules, for example by adding a high-MI (3 seems most logical) Rule with a text like:

> Any Rule Change which would cause a Rule with an MI lower than three that claims precedence over Rule 1482 is not allowed to take place, any Rule to the contrary notwithstanding.

References:
[<a name="ref1">1</a>] Agora ruleset.
[<a name="ref2">2</a>] Peter Suber, _The Paradox of Self-Amendment: A Study of Logic, Law, Omnipotence, and Change_. Peter Lang Publishing, 1990.