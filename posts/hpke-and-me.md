---
# HPKE and Me
##### _An intro into Hybrid Public Key Encryption_

## Asymmetric and Symmetric Key Encryption: A Refresher
>_In all of us lives two wolves: asymmetric and symmetric encryption._

### Symmetric Key Encryption

  __Symmetric key__ encryption is the simplest and oldest form of secure communication. It dates back to the [Caesar days](https://en.wikipedia.org/wiki/Caesar_cipher). 

The Caesar cipher is a encryption scheme that encrypts messages by applying a fixed char "rotation" for each character in the plaintext. Messages can be decrypted by applying the reverse of the "rotation key". These days keys are a lot more complex, but the idea of sharing a single key to decrypt AND encrypt a message still stands. 

Symmetric key encryption is cheap and efficient, but it has its draw backs:

- The biggest drawback is key distribution. Symmetric key schemes necessitate a way to communicate a key between two parties without interception from a third party. If the symmetric key gets out, all bets are off. Present and past communication (symmetric keys lack [forward secrecy]()) could be decrypted.

- There is no authentication that the sender is who they say they are. *Anyone* with the encryption key could send a message impersonating the sender and the recepient would have no clue. 
  > _This concept is known as "non-repudiation"._

- Scaling symmetric key communication is a nightmare. If one wanted to communicate with a _group_ of individuals, each member of that group would need their own private key to communicate with each other. The number of keys needed scales non-linearly:

        - 2 users (*1 key* A->B)
        - 3 users (*3 keys* {A->B, A->C, B->C})
        - 4 users (*6 keys* {A->B, A->C, A->D, B->C, B->D, C->D})
  Now imagine all of the infrastructure (storage AND distribution) needed to hand all of these keys out. Everytime a new member is added everyone needs their symmetric key. And if we need to do _key rotation_ (which we do) then just forget about it.

> **You (Probably):** "Uh, why don't they just _all_ use the same symmetric key?"
>
> If every individual in the party uses the same key and that key is
compromised, *everyones* communication is compromised. This is unacceptable in nearly every scenario. By giving every pair their own encrypted channel, one compromise doesn't invalidate our entire encryption model.

**TLDR:** Symmetric key encryption is cheap and easy to reason about on a small scale. However, it lacks the ability to provide a sufficient trust model (non-repudiation) and it scales poorly past a handfull of messengers.

## Asymmetric Key Encryption 
Assymetric encryption on the other hand utilizes two keys: a private key and a public key. The two parties (Alice and Bob) both generate a private and public key pair. To communicate they distribute the public key to each other. Messenges are encrypted via the public key and can only be decrypted via the private key. 

While assymetric key encryption is more computation expensive, it provides a number of benefits:

- Key distribution (the major problem with symmetric encryption) is easy now. Just advertise your public key to *everyone*. Malicious actors can't do much with the public key, aside from send encrypted messages. All of the prior, future, adn present communication is still impenetrable, because the private key is needed to decrypt and traffic. 

- Using multiple non-symmetric keys provides the ability to _authenicate_ the recipient. Only the person in posession of the private key is able to decrypt messages that were encrytped with the public key. This helps solve the non-repudiation aspect of the symmetric key scheme. Through some slightly more complicated magic, the sender's own private and public keypair could be used to authenticate the sender as well, but I won't be going into this here.

## Hybrid Public Key Encrytion (HPKE)
The astute among you may see where this is headed. Let's take a look at the lay of the land:

  - *Symmetric key* encryption is computationally cheap.
  - *Symmetric keys* are _difficult_ to distribute.
  - *Asymmetric keys* are more computationally expensive.
  - *Asymmetric keys* are _easy_ to distribute.

What if we put the pb with the j?
Enter *HPKE*:
Hybrid Public Key Encryption combines the inexpensiveness of symmetric key schemes with the robust security guarantees of asymmetric key schemes.

The flow is like this (I'll use a server <-> client model here):
  - The server generates a keypair{public_key, private_key}.
  - The public key is distributed _in plaintext_ to _everyone_.
  - A client can use the public key to _derive_ and _encapsulate_  a symmetric key that is sent along side its message (which is encrypted with the symmetric key)
  - The server can then use its private key to decap the symmetric key and decrypt the message.

Here we retain the encryption guarantees of asymmetric encryption, but without  requiring the user to generate a keypair. This process allows for quick "one shot" encryption messages to be sent with little overhead. A user can simply encrypt it's message via the public key, do a small computation to generate the symmetric key, and then send. Most of the cryptographic computations are moved server side, which is great for our current "mobile first" internet.

There's more to HPKE, but my laptop is dying and ShakeShack™️  is calling my name. I might revist this later.

--- 
#### References:
  - [RFC9180](https://datatracker.ietf.org/doc/rfc9180/)
  - [Cloudflare Blog]()
