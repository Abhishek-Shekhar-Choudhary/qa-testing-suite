describe('SauceDemo — checkout', () => {
  beforeEach(() => {
    cy.loginAsStandardUser();
    cy.get('[data-test="add-to-cart-sauce-labs-backpack"]').click();
    cy.get('[data-test="shopping-cart-link"]').click();
    cy.get('[data-test="checkout"]').click();
  });

  it('should complete purchase and show the order confirmation screen', () => {
    cy.get('[data-test="firstName"]').type('Jane');
    cy.get('[data-test="lastName"]').type('Tester');
    cy.get('[data-test="postalCode"]').type('90210');
    cy.get('[data-test="continue"]').click();
    cy.get('[data-test="finish"]').click();
    cy.get('[data-test="complete-header"]').should('contain', 'Thank you for your order!');
    cy.get('[data-test="back-to-products"]').should('be.visible');
  });
});
