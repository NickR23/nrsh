# HPKE and Me
##### _An intro into Hybrid Public Key Encryption_

## Symmetric Key Encryption: A Refresher
>_In all of us lives two wolves: asymmetric and symmetric encryption._

  __Symmetric key__ encryption is the simplest and oldest form of secure communication. It dates back to the [Caesar days](https://en.wikipedia.org/wiki/Caesar_cipher). 
The Caesar cipher is a encryption scheme that encrypts messages by applying a fixed char "rotation" for each character in the plaintext. Messages can be decrypted by applying the reverse of the "rotation key". These days keys are a lot more complex, but the idea of sharing a single key to decrypt AND encrypt a message still stands. 

Symmetric key encryption is cheap and efficient, but it has its draw backs:

- There is no authentication that the sender is who they say they are. *Anyone* with the encryption key could send a message impersonating the sender and the recepient would have no clue. 
  > _This concept is known as "non-repudiation"._

- Scaling symmetric key communication is a nightmare. If one wanted to communicate with a _group_ of individuals, each member of that group would need their own private key to communicate with each other. The number of keys needed scales non-linearly:

        - 2 users (*1 key* A->B)
        - 3 users (*3 keys* {A->B, A->C, B->C})
        - 4 users (*6 keys* {A->B, A->C, A->D, B->C, B->D, C->D})

  > "Uh, why don't they just use the _same_ symmetric key?" -You (Probably)
> **You (Probably):** "Uh, why don't they just use the same symmetric key?"

> If every individual in the party uses the same key, if that key is
compromised *everyone's* communication is compromised. This is unacceptable in
nearly all scenarios.

     - If every individual in the party uses the same key, if that key is compormised *everyone's* communication is compromised. This is unacceptable in nearly all scenarios.

#### References:
  - [RFC9180](https://datatracker.ietf.org/doc/rfc9180/)
