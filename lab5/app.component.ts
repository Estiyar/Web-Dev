import { Component } from '@angular/core';
import { ProductListComponent } from './products/product-list.component';
import { CATEGORIES } from './products/products.data';
import { PRODUCTS } from './products/products.data';
import { Category } from './products/category.model';
import { Product } from './products/product.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ProductListComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  categories: Category[] = CATEGORIES;
  allProducts: Product[] = PRODUCTS;
  selectedCategoryId: number | null = null;

  get filteredProducts(): Product[] {
    return this.allProducts.filter(p => p.categoryId === this.selectedCategoryId);
  }

  selectCategory(id: number) {
    this.selectedCategoryId = id;
  }
}
