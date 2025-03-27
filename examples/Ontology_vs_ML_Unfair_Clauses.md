# Tool Comparison: Claudette vs TOSL

## 1. Objective of the Analysis

This analysis compares the performance and capabilities of two tools in detecting potentially unfair clauses in SaaS agreements:

- **Claudette**: A machine learning-based tool that classifies sentences into predefined categories of potentially unfair clauses.
- **TOSL**: An ontology that models legal agreements and uses SPARQL queries to semantically detect potentially unfair clauses.

- **Corpus Used**:  
  - [Elsevier API Service Agreement](https://dev.elsevier.com/api_service_agreement.html)  
  - [OpenAI Terms of Use (EU)](https://openai.com/policies/eu-terms-of-use/)

---

## 2. Initial Evaluation of the Tools

| Evaluation Criteria           | Claudette                                           | TOSL                                                        |
|------------------------------|-----------------------------------------------------|-------------------------------------------------------------|
| **Category Coverage**        | 8 predefined types                                  | Flexible, based on the ontology design                      |
| **Accuracy**                 | Medium, dependent on natural language limitations | High if the knowledge graph is well-modeled                        |
| **Interpretability**         | Low (black-box ML model)                            | High (explicit queries and traceability)                    |
| **Customization**            | Limited                                             | High (extensible and adaptable)                             |
| **Processing Time**          | Fast                                                | Fast                                                        |
| **Ease of Use**              | Very easy (plain text input)                        | Requires knowledge of ontologies and SPARQL                 |

---

## 3. Case Study: Elsevier API Service Agreement

### Analysis Approach  
The following section analyses clauses identified as potentially unfair by either **Claudette** or **TOSL**, organised by the type of unfair term.

<details>
<summary>Arbitration</summary>
The contract does not contain any clauses related to Arbitration that could be considered potentially unfair.
</details>

<details>
<summary>Choice of Law</summary>

- **Term**:  
  _"This Agreement will be governed by and construed in accordance with the laws of The Netherlands, and the parties irrevocably consent to the exclusive jurisdiction of the courts of The Netherlands with respect to any action or suit arising out of or pertaining to this Agreement (except where local law requires)."_

  - **Claudette**: Detected  
  - **TOSL**: Not detected  
  - **Justification**: This clause refers to the applicable law—in this case, Netherlands Law. However, it explicitly allows for the application of local law where required. For that reason, it should not be considered unfair under consumer protection standards.

</details>

<details>
<summary>Content Removal</summary>
The contract does not contain any clauses related to Content Removal that could be considered potentially unfair.
</details>

<details>
<summary>Contract by Using</summary>
The contract does not contain any clauses related to Contract by Using that could be considered potentially unfair.
</details>

<details>
<summary>Jurisdiction</summary>

- **Term**:  
  _"This Agreement will be governed by and construed in accordance with the laws of The Netherlands, and the parties irrevocably consent to the exclusive jurisdiction of the courts of The Netherlands with respect to any action or suit arising out of or pertaining to this Agreement (except where local law requires)."_

  - **Claudette**: Detected  
  - **TOSL**: Not detected  
  - **Justification**: This clause defines the jurisdiction as the courts of The Netherlands. However, it includes an exception for cases where local law requires otherwise. Therefore, it respects the consumer's right to litigate in their country of residence and should not be considered unfair.

</details>

<details>
<summary>Limitation of Liability</summary>

- **Term**:  
  _"3.2 The Developer will be solely responsible and hold Elsevier harmless for all costs, expenses, losses and liabilities incurred, and activities undertaken by the Developer in connection with the API Service"_

  - **Claudette**: Not Detected  
  - **TOSL**: Detected  
  - **Justification**: Elsevier disclaims all liability, even in situations involving possible negligence or deficiencies in the service.


- **Term**:  
  _"Except as expressly stated in this Agreement, each party disclaims all liability to the other party in connection with the parties' performance of this Agreement and in no event will the infringing party be liable to the other party for special, indirect or consequential damages including but not limited to loss of profits, loss of business or unfitness for user purposes."_

  - **Claudette**: Detected  
  - **TOSL**: Detected  
 - **Justification**: This clause broadly excludes all liability between the parties, including for indirect or consequential damages such as loss of profits or business.
</details>

<details>
<summary>Unilateral Change</summary>

- **Term**:  
  _"1.2 Elsevier reserves the right, at its sole discretion, to **change** the terms of this Agreement at any time with reasonable advance notice given to the Developer..."_

  - **Claudette**: Detected  
  - **TOSL**: Detected  
  - **Justification**: This clause refers to a _Unilateral Change_ of terms, made at Elsevier’s sole discretion, without requiring justification or prior notice.

</details>

<details>
<summary>Unilateral Termination</summary>

- **Term**:  
  _"1.2 Elsevier reserves the right, at its sole discretion, to **change** the terms of this Agreement at any time with reasonable advance notice given to the Developer..."_

  - **Claudette**: Detected  
  - **TOSL**: Not detected  
  - **Justification**: This clause refers to a _Unilateral Change_ of terms rather than a _Termination_. TOSL distinguishes between these nuances based on semantic modeling.

---

- **Term**:  
  _"2.1 Elsevier retains the right to immediately **suspend** the Application's access to the API Service if, in Elsevier's sole judgment: the Application's usage of the API Service negatively affects the availability or performance of the API Service, or the Application is in breach of the API's Content Usage Policies on http://dev.elsevier.com/policy.html"_

  - **Claudette**: Detected  
  - **TOSL**: Detected  
  - **Justification**: Elsevier may suspend access with justification, but without prior notice.

---

- **Term**:  
  _"2.2 In a situation of **breach of the terms and conditions** of this Agreement, Elsevier reserves the right to block, change, suspend, remove or disable access to the APIs and any of its services at any time upon **reasonable notice** to Developer."_

  - **Claudette**: Detected  
  - **TOSL**: Not detected  
  - **Justification**: Elsevier may suspend access with justification and prior notice. However, such clauses may be considered misleading, as the provider retains significant discretionary power to determine contract termination without offering the customer an opportunity to contest it.

---

- **Term**:  
  _"2.3 Elsevier reserves the right to **deactivate** API Keys that have not been used to access the APIs for 90 days."_

  - **Claudette**: Not detected  
  - **TOSL**: Detected  
  - **Justification**: Elsevier may suspend access solely due to inactivity over a 90-day period.

---

- **Term**:  
  _"The term of this Agreement shall commence on the date on which the Developer has accepted this Agreement and shall continue until either party **terminates** the Agreement in writing or the API Key is deactivated by Elsevier."_

  - **Claudette**: Not detected  
  - **TOSL**: Detected  
  - **Justification**: Elsevier has the right to terminate the agreement with written notice.

</details>

---

### Summary of Comparative Detection Results

| Type of Potentially Unfair Clause | Claudette (Number of Clauses) | TOSL (Number of Clauses) |
|-----------------------------------|-----------------------------|------------------------|
| Arbitration                       | 0                           | 0                      |
| Choice of Law                     | 1                           | 0                      |
| Content Removal                   | 0                           | 0                      |
| Contract by Use                   | 0                           | 0                      |
| Jurisdiction                      | 1                           | 0                      |
| Limitation of Liability           | 1                           | 2                      |
| Unilateral Change                 | 1                           | 1                      |
| Unilateral Termination            | 3                           | 3                      |
| **Total**                         | **7**                       | **6**             |

---

## 4. Case Study: OpenAI Terms of Use (EU)

### Analysis Approach  
The following section analyses clauses identified as potentially unfair by either **Claudette** or **TOSL**, organised by the type of unfair term.

<details>
<summary>Arbitration</summary>
The contract does not contain any clauses related to Arbitration that could be considered potentially unfair.
</details>

<details>
<summary>Choice of Law</summary>

- **Term**:  
  _"Governing law (business use). California law will govern these Terms except for its conflicts of laws principles. All claims arising out of or relating to these Terms will be brought exclusively in the federal or state courts of San Francisco, California."_

  - **Claudette**: Detected  
  - **TOSL**: Not Detected  
  - **Justification**: This clause applies to business accounts, not individual consumers. In B2B relationships, consumer protection laws do not apply, and parties have more freedom to choose governing law and jurisdiction.

</details>

<details>
<summary>Content Removal</summary>

- **Term**:  
  _"Once your account is transferred, the organisation’s administrator will be able to control your account, including being able to access Content (defined below) and restrict or remove your access to the account. "_

  - **Claudette**: detected  
  - **TOSL**: Not Detected  
  - **Justification**: This clause grants the customer the right to transfer their account, with the administrator having full control. It does not imply that OpenAI can delete the user’s content without notice or justification.

- **Term**:  
  _"If we terminate your account, we will make reasonable efforts to notify you in advance so you can export your Content or your data from the Services, unless it is not appropriate for us to do so, we reasonably believe that continued access to your account will cause damage to OpenAI or anyone else, or we are legally prohibited from doing so."_

  - **Claudette**: Detected  
  - **TOSL**: Partial Detected  
  - **Justification**: This clause is not considered unfair because it states that the provider will make reasonable efforts to notify the customer before terminating the account. It does not refer to the removal of user content.

- **Term**:  
  _"We may delete or disable content alleged to be infringing and may terminate accounts of repeat infringers."_

  - **Claudette**: Detected  
  - **TOSL**: Not Detected  
  - **Justification**: This clause refers to allegedly infringing content and the termination of repeat infringers, which is a standard and legally required practice. In fact, it empowers the customer to file a complaint if they believe their intellectual property rights are being violated.

</details>


<details>
<summary>Contract by Using</summary>
The contract does not contain any clauses related to Contract by Using that could be considered potentially unfair.
</details>


<details>
<summary>Jurisdiction</summary>

- **Term**:  
  _"Governing law (business use). California law will govern these Terms except for its conflicts of laws principles. All claims arising out of or relating to these Terms will be brought exclusively in the federal or state courts of San Francisco, California."_

  - **Claudette**: Detected  
  - **TOSL**: Not Detected  
  - **Justification**: This clause applies to business accounts, not individual consumers. In B2B relationships, consumer protection laws do not apply, and parties have more freedom to choose governing law and jurisdiction.

</details>


<details>
<summary>Limitation of Liability</summary>

- **Term**:  
  _"Third Party Services and Third Party Output are subject to their own terms, and we are not responsible for them."_

  - **Claudette**: Not Detected  
  - **TOSL**: Detected  
  - **Justification**: OpenAI disclaims any responsibility for damages that may be caused by third-party services included within its own services.

 - **Term**:  
  _"Given the probabilistic nature of machine learning, use of our Services may in some situations result in Output that does not accurately reflect real people, places, or facts."_

  - **Claudette**: Not Detected  
  - **TOSL**: Detected  
  - **Justification**: OpenAI disclaims responsibility for both the accuracy of the responses and their content.


- **Term**:  
  _"We do not promise to offer the Services forever or in their current form for any particular period of time."_

  - **Claudette**: Not Detected  
  - **TOSL**: Detected  
  - **Justification**: OpenAI disclaims responsibility for the continuity of the service.

- **Term**:  
  _"We do not take responsibility for loss or damage caused by events beyond our reasonable control."_

  - **Claudette**: Detected  
  - **TOSL**: Detected  
  - **Justification**: OpenAI disclaims responsibility for both indirect damages and losses.


- **Term**:  
  _"NEITHER WE NOR ANY OF OUR AFFILIATES OR LICENSORS WILL BE LIABLE FOR ANY INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR EXEMPLARY DAMAGES, INCLUDING DAMAGES FOR LOSS OF PROFITS, GOODWILL, USE, OR DATA OR OTHER LOSSES, EVEN IF WE HAVE BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. OUR AGGREGATE LIABILITY UNDER THESE TERMS WILL NOT EXCEED ​​THE GREATER OF THE AMOUNT YOU PAID FOR THE SERVICE THAT GAVE RISE TO THE CLAIM DURING THE 12 MONTHS BEFORE THE LIABILITY AROSE OR ONE HUNDRED DOLLARS ($100). THE LIMITATIONS IN THIS SECTION APPLY ONLY TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW."_

  - **Claudette**: Detected  
  - **TOSL**: Not Detected 
  - **Justification**: This limitation of liability applies only in a B2B context. Therefore, consumer protection laws do not apply.

</details>


<details>
<summary>Unilateral Change</summary>

- **Term**:  
  _"We may change our prices from time to time. If we increase our subscription prices, we will give you at least 30 days’ notice and any price increase will take effect on your next renewal so that you can cancel if you do not agree to the price increase."_

  - **Claudette**: Detected  
  - **TOSL**: Detected  
  - **Justification**: This clause allows the provider to increase prices with 30 days’ notice and gives the customer the option to cancel, which helps maintain fairness. However, the provider is not required to justify the change, which gives them unilateral control and could place the customer at a disadvantage.

- **Term**:  
  _"We are continuously working to develop and improve our Services. We may update these Terms or our Services accordingly from time to time...(continue)"_

  - **Claudette**: Detected  
  - **TOSL**: Not Detected  
  - **Justification**: The clause provides reasons for changes, 30 days’ notice, and applies changes only going forward. However, since the user’s only option is to stop using the service, and the provider retains broad discretion, it may be considered borderline unfair.

</details>

<details>
<summary>Unilateral Termination</summary>

- **Term**:  
  _"Once your account is transferred, the organisation’s administrator will be able to control your account, including being able to access Content (defined below) and restrict or remove your access to the account. "_

  - **Claudette**: Detected  
  - **TOSL**: Not Detected  
  - **Justification**: This clause allows the customer to transfer their account, with the administrator having full control. It does not imply that OpenAI can unilaterally terminate the contract; it partly reflects a request from the customer.

- **Term**:  
  _"If your payment cannot be completed, we may downgrade your account or suspend your access to our Services until payment is received"_

  - **Claudette**: Detected  
  - **TOSL**: Not Detected  
  - **Justification**: This clause establishes a reasonable consequence for non-payment. It is not considered unfair, as access is only suspended or downgraded until payment is received.

- **Term**:  
  _"We may take action to suspend or terminate your access to our Services or close your account if we determine, acting reasonably and objectively"_

  - **Claudette**: Detected  
  - **TOSL**: Partial Detected  
  - **Justification**: This clause provides a reasonable set of grounds for suspending access to the services, as long as prior notice is given and the user has an opportunity to appeal.

- **Term**:  
  _"If we terminate your account, we will make reasonable efforts to notify you in advance so you can export your Content or your data from the Services, unless it is not appropriate for us to do so, we reasonably believe that continued access to your account will cause damage to OpenAI or anyone else, or we are legally prohibited from doing so."_

  - **Claudette**: Detected  
  - **TOSL**: Not Detected  
  - **Justification**: This clause is not considered unfair because it states that the provider will make reasonable efforts to notify the customer before terminating the account.

- **Term**:  
  _"We may delete or disable content alleged to be infringing and may terminate accounts of repeat infringers."_

  - **Claudette**: Detected  
  - **TOSL**: Not Detected  
  - **Justification**: This clause refers to allegedly infringing content and the termination of repeat infringers, which is a standard and legally required practice. In fact, it empowers the customer to file a complaint if they believe their intellectual property rights are being violated.

- **Term**:  
  _"If you are not satisfied, you have the right to terminate your relationship with OpenAI and stop using our Services at any time."_

  - **Claudette**: Detected  
  - **TOSL**: Not Detected  
  - **Justification**: This clause grants the customer the right to terminate the contract at any time if they are not satisfied. Since it empowers the user rather than limits their rights, it cannot be considered unfair.

</details>

---

### Summary of Comparative Detection Results

| Type of Potentially Unfair Clause | Claudette (Number of Clauses) | TOSL (Number of Clauses) |
|-----------------------------------|-----------------------------|------------------------|
| Arbitration                       | 0                           | 0                      |
| Choice of Law                     | 1                           | 0                      |
| Content Removal                   | 3                           | 0                      |
| Contract by Use                   | 0                           | 0                      |
| Jurisdiction                      | 1                           | 0                      |
| Limitation of Liability           | 2                           | 4                      |
| Unilateral Change                 | 2                           | 1                      |
| Unilateral Termination            | 6                           | 1                      |
| **Total**                         | **15**                      | **6**                  |
