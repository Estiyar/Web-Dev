import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../models/product.model';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  // Массив товаров с Kaspi.kz (с рабочими изображениями)
  products: Product[] = [
    {
      id: 1,
      name: 'Apple iPhone 15 Pro Max 256GB',
      description: 'Новейший флагманский смартфон от Apple с титановым корпусом и мощным процессором A17 Pro.',
      price: 720125,
      rating: 4.9,
      image: 'https://unsplash.com/photos/an-iphone-is-sitting-on-top-of-a-box-LunVPm34ly4',
      images: [
        'https://images.unsplash.com/photo-1695619575284-72db5dd6439e?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGlwaG9uZSUyMDE1JTIwcHJvfGVufDB8fDB8fHww',
        'https://images.unsplash.com/photo-1695619575333-fc73accd441e?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGlwaG9uZSUyMDE1JTIwcHJvfGVufDB8fDB8fHww',
        'https://images.unsplash.com/photo-1703133431079-8477009d42b2?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTV8fGlwaG9uZSUyMDE1JTIwcHJvfGVufDB8fDB8fHww'
      ],
      link: 'https://kaspi.kz/shop/p/apple-iphone-15-pro-max-256gb-seryi-113138420/?c=750000000'
    },
    {
      id: 2,
      name: 'Samsung Galaxy S24 Ultra 256GB',
      description: 'Премиальный смартфон Samsung с AI-функциями, S Pen и потрясающей камерой 200 МП.',
      price: 648835,
      rating: 4.8,
      image: 'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400',
      images: [
        'https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=400',
        'https://images.unsplash.com/photo-1705585174953-9b2aa8afc174?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8U2Ftc3VuZyUyMEdhbGF4eSUyMFMyNCUyMFVsdHJhfGVufDB8fDB8fHww',
        'https://images.unsplash.com/photo-1709744722656-9b850470293f?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8U2Ftc3VuZyUyMEdhbGF4eSUyMFMyNCUyMFVsdHJhfGVufDB8fDB8fHww'
      ],
      link: 'https://kaspi.kz/shop/p/samsung-galaxy-s24-ultra-5g-12-gb-256-gb-seryi-116043556/?c=750000000'
    },
    {
      id: 3,
      name: 'Dyson V15 Detect Absolute',
      description: 'Беспроводной пылесос с лазерным детектором пыли и мощным двигателем для идеальной чистоты.',
      price: 315000,
      rating: 4.7,
      image: 'https://images.unsplash.com/photo-1558317374-067fb5f30001?w=400',
      images: [
        'https://images.unsplash.com/photo-1558317374-067fb5f30001?w=400',
        'https://images.unsplash.com/photo-1527515637462-cff94eecc1ac?w=400',
        
      ],
      link: 'https://kaspi.kz/shop/p/dyson-v15-detect-absolute-sv47-serebristyi-113691132/?c=750000000'
    },
    {
      id: 4,
      name: 'MacBook Air M2 13" 256GB',
      description: 'Ультратонкий ноутбук от Apple на чипе M2 с невероятной производительностью и автономностью.',
      price: 429279 ,
      rating: 4.9,
      image: 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400',
      images: [
        'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400',
        'https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?w=400',
        
      ],
      link: 'https://kaspi.kz/shop/p/apple-macbook-air-13-2022-13-6-16-gb-ssd-256-gb-macos-mc7x4-133963854/?c=750000000'
    },
    {
      id: 5,
      name: 'PlayStation 5 Slim Digital Edition',
      description: 'Игровая консоль нового поколения с невероятной графикой и быстрой загрузкой игр.',
      price: 319953,
      rating: 4.8,
      image: 'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400',
      images: [
        'https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=400',
        'https://images.unsplash.com/photo-1622297845775-5ff3fef71d13?w=400',
        'https://images.unsplash.com/photo-1607853202273-797f1c22a38e?w=400'
      ],
      link: 'https://kaspi.kz/shop/p/sony-playstation-5-slim-digital-geimpad-charging-station-117975912/?c=750000000'
    },
    {
      id: 6,
      name: 'Apple AirPods Pro 2nd Gen',
      description: 'Беспроводные наушники с активным шумоподавлением и пространственным звуком.',
      price: 107899,
      rating: 4.9,
      image: 'https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=400',
      images: [
        'https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=400',
        
      ],
      link: 'https://kaspi.kz/shop/p/naushniki-apple-airpods-pro-2nd-generation-with-wireless-magsafe-charging-case-belyi-113677582/?c=750000000'
    },
    {
      id: 7,
      name: 'LG 43NANO80A6B',
      description: 'Умный OLED-телевизор с идеальным черным цветом, HDR и встроенными сервисами.',
      price: 239307 ,
      rating: 4.8,
      image: 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400',
      images: [
        'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=400',
        ,'https://images.unsplash.com/photo-1461151304267-38535e780c79?w=400'
      ],
      link: 'https://kaspi.kz/shop/p/lg-43nano80a6b-109-sm-chernyi-138971688/?c=750000000'
    },
    {
      id: 8,
      name: 'Samsung Galaxy Watch 8 Classic',
      description: 'Премиальные умные часы с вращающимся безелем, мониторингом здоровья и долгой автономностью.',
      price: 159778 ,
      rating: 4.7,
      image: 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400',
      images: [
        
        'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400',
        
      ],
      link: 'https://kaspi.kz/shop/p/samsung-galaxy-watch-8-classic-46-mm-serebristyi-chernyi-142950290/?c=750000000'
    },
    {
      id: 9,
      name: 'DeLonghi Magnifica S ECAM 22.110',
      description: 'Автоматическая кофемашина для приготовления эспрессо и капучино дома.',
      price: 292390,
      rating: 4.6,
      image: 'https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=400',
      images: [
        'https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=400',
        'https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=400',
        'https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=400'
      ],
      link: 'https://kaspi.kz/shop/p/kofemashina-delonghi-magnifica-start-ecam-220-60-b-chernyi-117220826/?c=750000000'
    },
    {
      id: 10,
      name: 'Xiaomi Robot Vacuum S10+',
      description: 'Робот-пылесос с самоочисткой, лазерной навигацией и влажной уборкой.',
      price: 136970,
      rating: 4.7,
      image: 'https://plus.unsplash.com/premium_photo-1729006559482-d289e4385b1e?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Um9ib3QlMjBWYWN1dW18ZW58MHx8MHx8fDA%3D',
      images: [
        'https://plus.unsplash.com/premium_photo-1729006559482-d289e4385b1e?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8Um9ib3QlMjBWYWN1dW18ZW58MHx8MHx8fDA%3D',
        'https://images.unsplash.com/photo-1762859731349-c9ff2808b672?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fFJvYm90JTIwVmFjdXVtfGVufDB8fDB8fHww',
        
      ],
      link: 'https://kaspi.kz/shop/p/xiaomi-robot-vacuum-s10-bhr6368eu-belyi-108100032/?c=750000000'
    }
  ];

  // Текущая выбранная галерея для каждого продукта
  currentImageIndex: { [key: number]: number } = {};

  // Инициализация галереи
  ngOnInit() {
    this.products.forEach(product => {
      this.currentImageIndex[product.id] = 0;
    });
  }

  // Получить текущее изображение для продукта
  getCurrentImage(product: Product): string {
    const index = this.currentImageIndex[product.id] || 0;
    return product.images[index];
  }

  // Переключить на следующее изображение
  nextImage(product: Product, event: Event) {
    event.stopPropagation();
    const currentIndex = this.currentImageIndex[product.id] || 0;
    this.currentImageIndex[product.id] = (currentIndex + 1) % product.images.length;
  }

  // Переключить на предыдущее изображение
  prevImage(product: Product, event: Event) {
    event.stopPropagation();
    const currentIndex = this.currentImageIndex[product.id] || 0;
    this.currentImageIndex[product.id] = currentIndex === 0 
      ? product.images.length - 1 
      : currentIndex - 1;
  }

  // Выбрать конкретное изображение
  selectImage(productId: number, index: number, event: Event) {
    event.stopPropagation();
    this.currentImageIndex[productId] = index;
  }

  // Поделиться в WhatsApp
  shareOnWhatsApp(product: Product, event: Event) {
    event.stopPropagation();
    const message = `Посмотри на этот товар: ${product.name}`;
    const url = encodeURIComponent(product.link);
    const text = encodeURIComponent(message);
    window.open(`https://wa.me/?text=${text}%20${url}`, '_blank');
  }

  // Поделиться в Telegram
  shareOnTelegram(product: Product, event: Event) {
    event.stopPropagation();
    const url = encodeURIComponent(product.link);
    const text = encodeURIComponent(product.name);
    window.open(`https://t.me/share/url?url=${url}&text=${text}`, '_blank');
  }

  // Открыть товар на Kaspi.kz
  openProduct(link: string) {
    window.open(link, '_blank');
  }

  // Сгенерировать массив для звёзд рейтинга
  getStars(rating: number): boolean[] {
    return Array(5).fill(false).map((_, index) => index < Math.round(rating));
  }
}
