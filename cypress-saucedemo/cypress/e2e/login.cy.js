describe('SauceDemo — authentication', () => {
  it('should open the product catalog after successful login', () => {
    cy.loginAsStandardUser();
    cy.url().should('include', '/inventory.html');
    cy.get('[data-test="title"]').should('contain', 'Products');
  });

  it('should show an error and not navigate to inventory when the password is wrong', () => {
    cy.login('standard_user', 'wrong_password');
    cy.get('[data-test="error"]').should('be.visible');
    cy.url().should('not.include', 'inventory');
  });
});
