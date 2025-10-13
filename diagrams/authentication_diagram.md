```mermaid
flowchart TD
A(Client sends HTTP Basic credentials) --> B[Authenticate Function]
B --> C{Username matches 'havryliuk'?}
C -- No --> F[Raise 401 Unauthorized]
C -- Yes --> D[Get Password]
D --> D1{PASSWORD in .env?}
D1 -- Yes --> E[Use .env password]
D1 -- No --> E1[Fetch password from AWS Secrets Manager]
E1 --> E2[Use fetched password]
E --> H[Compare provided password to correct password]
E2 --> H
H{Password matches?}
H -- No --> F
H -- Yes --> G[Authentication successful\nReturn username]
