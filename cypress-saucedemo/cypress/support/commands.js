/**
 * Logs in via the SauceDemo UI. Keeps specs focused on behavior after auth.
 */
Cypress.Commands.add('login', (username, password) => {
  cy.visit('/');
  cy.get('[data-test="username"]').clear().type(username);
  cy.get('[data-test="password"]').clear().type(password);
  cy.get('[data-test="login-button"]').click();
});

Cypress.Commands.add('loginAsStandardUser', () => {
  cy.login('standard_user', 'secret_sauce');
});

/**
 * The inventory hamburger menu has no data-test attribute on the control in the stock demo;
 * the React id is the documented stable locator used across Sauce Labs examples.
 */
Cypress.Commands.add('openSideMenu', () => {
  cy.get('#react-burger-menu-btn').should('be.visible').click();
});

Cypress.Commands.add('logoutViaUi', () => {
  cy.openSideMenu();
  cy.get('[data-test="logout-sidebar-link"]').should('be.visible').click();
});
