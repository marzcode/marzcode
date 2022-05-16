# Marzcode
Ground Breaking encryption with fully customizable keys that was designed with both speed and security taken into consideration.


So I am still unsure of what do do with this project.
and am now entering the beta testing stage of seeing if the code can withstand various known attacks.

The crypto I have built allows you enter your own keys.
It then takes these keys and uses them to encrypt your plain text message.

The algorithm generates its own code chart
and this needs to be shared with each party from the very begining
along with a text file containing a list of keys used by various different ciphers

Then when the first message is created, it deducts from the chart the equations it used (images a reel of raffle tickets)

so that when the recipient of the message replys they will be replying using new equations.

when the chart is first enerated it contains a fixed nunber of equations,
However the parties envolved in communication
are able to transmit new algorithms to generate more coded charts
which will allow them to continue communicating.

That is only stage one of the algorithm.

Stage two then takes the output of these chart algorithms

and applies a groud breaking block cipher
that first divides the output into fixed blocks
and then runs a unique cypher on each seperate block.

These blocks are then broken down into smaller chunks and 
and all the smaller chunks are placed togeether

The chunks are then rearranged and built back up into larger chunks
where a furhter cypher is then applied.

The blocks are then broken back up into smaller chunks
and a cypher is then applied to each small chunk

These small chunks are then rearranged into a new order

and a final cipher is applied.

Further I would like to add that although my algorithm is symmetric in the since that
the same keys are use for encryption and decryption.

The same message encoded using the same keys and code charts will produce various different encrypted outputs.

Almost like the opposit of what happens when you use hashing


