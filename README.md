# CS-325-Project-1-Adjusted-Binary-Seach-Method

Project Prompt:
There is going to be an art exhibition in Corvallis. The organizers announced that they are
going to hold the exhibition for D days. People have registered to attend the event in groups.
Overall, n groups of people registered with g1, g2, . . . , gn members; for each i < j, group i has
registered before group j, so they should have priority for attending the event. The organizers are
now wondering what is the minimum number of people they should admit each day so that
(1) all groups can attend the event,
(2) all members of a group attend the exhibition together (on the same day), and
(3) the order of the groups is preserved: for any i < j group i sees the exhibition earlier than or
at the same day as group j.
We would like to design an algorithm that helps the organizer to find the minimum possible
daily attendance they need to allow in order to finish the event in D days. Specifically, we want to
solve the following problems.
(A) Design an O(n log G) time algorithm for computing the minimum number of admittance per
day to finish the exhibition in D days; n is the number of groups and G is the total number
of people registered for the event: G = ∑ni=1 gi.
(B) What is the most efficient algorithm for this problem that you can find whose running time
is only a function of n, with no dependence to G?
