import { Component, Input, OnChanges } from '@angular/core';
import { ProductItemComponent } from './product-item.component';
import { Product } from './product.model';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [ProductItemComponent],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css',
})
export class ProductListComponent implements OnChanges {
  @Input() products: Product[] = [];

  localProducts: Product[] = [];

  ngOnChanges() {
    this.localProducts = [...this.products];
  }

  onDelete(id: number) {
    this.localProducts = this.localProducts.filter(p => p.id !== id);
  }
}
