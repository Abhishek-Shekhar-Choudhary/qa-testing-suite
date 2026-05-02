describe('SauceDemo — inventory catalog', () => {
  beforeEach(() => {
    cy.loginAsStandardUser();
  });

  it('should list products in ascending price order when Price (low to high) is selected', () => {
    cy.get('[data-test="product-sort-container"]').select('lohi');
    cy.get('[data-test="inventory-item-price"]').then(($prices) => {
      const values = [...$prices].map((el) =>
        Number.parseFloat(el.innerText.replace(/[^0-9.]/g, ''), 10),
      );
      expect(values.length, 'catalog should expose at least two prices').to.be.above(1);
      const sortedAsc = [...values].sort((a, b) => a - b);
      expect(values, 'visible prices should be non-decreasing after low-to-high sort').to.deep.equal(sortedAsc);
    });
  });
});
