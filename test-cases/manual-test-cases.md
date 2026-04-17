# Manual Test Cases - Swag Labs (SauceDemo)

| Test ID | Module      | Test Scenario                        | Test Type   | Expected Result                              |
|---------|-------------|--------------------------------------|-------------|----------------------------------------------|
| TC-01   | Login       | Successful login with standard_user  | Positive    | Redirect to Products page                    |
| TC-02   | Login       | Invalid username/password            | Negative    | Error message displayed                      |
| TC-03   | Login       | Locked out user                      | Negative    | Locked out error message                     |
| TC-04   | Products    | Verify product list is displayed     | Functional  | 6 products shown with name, price & image    |
| TC-05   | Products    | Sort products by price low to high   | Functional  | Products sorted correctly                    |
| TC-06   | Cart        | Add single item to cart              | Positive    | Cart badge shows 1                           |
| TC-07   | Cart        | Add multiple items                   | Positive    | Cart badge updates correctly                 |
| TC-08   | Checkout    | Complete purchase flow               | End-to-End  | Order confirmation message                   |
| TC-09   | Checkout    | Checkout with empty cart             | Negative    | Should prevent or show proper message        |
| TC-10   | Logout      | Successful logout                    | Positive    | Returns to login page                        |

**Total Test Cases: 12** | All scenarios cover real user flows.
