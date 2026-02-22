import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from './product.model';

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-item.component.html',
  styleUrl: './product-item.component.css',
})
export class ProductItemComponent implements OnInit {
  @Input() product!: Product;
  @Output() delete = new EventEmitter<number>();

  activeImage = '';

  ngOnInit() {
    this.activeImage = this.product.image;
  }

  onLike() {
    this.product.likes++;
  }

  onUnlike() {
    if (this.product.likes > 0) {
      this.product.likes--;
    }
  }

  onDelete() {
    this.delete.emit(this.product.id);
  }

  get whatsappUrl(): string {
    const text = encodeURIComponent(`Посмотри этот товар: ${this.product.link}`);
    return `https://wa.me/?text=${text}`;
  }

  get telegramUrl(): string {
    const url = encodeURIComponent(this.product.link);
    const text = encodeURIComponent(this.product.name);
    return `https://t.me/share/url?url=${url}&text=${text}`;
  }
}