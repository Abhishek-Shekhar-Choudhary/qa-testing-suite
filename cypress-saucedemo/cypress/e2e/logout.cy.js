describe('SauceDemo — session', () => {
  it('should return to the login screen after logging out from inventory', () => {
    cy.loginAsStandardUser();
    cy.logoutViaUi();
    cy.url().should('match', /saucedemo\.com\/?$/);
    cy.get('[data-test="login-button"]').should('be.visible');
  });
});
