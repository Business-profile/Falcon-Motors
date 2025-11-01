# Falcon Motors - Automotive Repair & Maintenance Website

## Overview
Falcon Motors is a professional automotive repair and maintenance service website featuring a modern, responsive design with a distinctive yellow brand identity. The website showcases expert technicians, comprehensive services, and customer testimonials.

## Brand Identity
- **Brand Name:** Falcon Motors
- **Primary Color:** #FFF316 (Falcon Yellow) - Used for CTAs, highlights, and active states
- **Secondary Color:** #1A1A1A (Premium Charcoal) - Used for navigation and strong contrasts
- **Light Color:** #F8F9FA (Clean off-white) - Used for backgrounds and subtle elements
- **Dark Color:** #0D0D0D (True black) - Used for text on yellow backgrounds for optimal readability

## Features
- **Responsive Design:** Fully responsive layout that adapts to desktop, tablet, and mobile devices
- **Modern Animations:** Powered by WOW.js and Animate.css for smooth scroll-triggered animations
- **Interactive Components:**
  - Hero carousel with multiple slides
  - Service navigation tabs with image galleries
  - Team member cards with social media hover overlays
  - Testimonial carousel with automatic rotation
  - Animated counter statistics
  - Date/time picker for booking forms
  - Sticky navigation bar
  - Back-to-top button

## Pages Included
1. **index.html** - Homepage with hero carousel, services, about section, booking form, team, and testimonials
2. **about.html** - About Us page with company information and team highlights
3. **service.html** - Services page with detailed service tabs
4. **booking.html** - Service booking page with date/time picker
5. **team.html** - Team/Technicians showcase page
6. **testimonial.html** - Customer testimonials carousel page
7. **contact.html** - Contact page with map, contact form, and multiple email addresses
8. **404.html** - Custom 404 error page

## Technology Stack
- **Framework:** Bootstrap 5.0.0
- **JavaScript Libraries:**
  - jQuery 3.4.1
  - WOW.js (scroll animations)
  - Owl Carousel 2 (testimonials carousel)
  - Counter-Up (animated numbers)
  - Tempus Dominus Bootstrap 4 (date/time picker)
  - jQuery Easing (smooth animations)
  - jQuery Waypoints (scroll triggers)
- **Icons:** Font Awesome 5.10.0, Bootstrap Icons
- **Fonts:** Google Fonts (Barlow, Ubuntu)

## Color Accessibility
All yellow (#FFF316) elements have been carefully designed for accessibility:
- **Yellow buttons** feature black text for maximum readability
- **Yellow backgrounds** always pair with dark/black text
- **Navigation bar** uses dark background with light text
- **Active states** maintain clear contrast ratios (WCAG AA compliant)
- **Hover effects** provide visual feedback with proper color contrasts

## File Structure
```
carserv-1.0.0/
├── css/
│   ├── bootstrap.min.css       # Bootstrap framework
│   └── style.css               # Custom styles and color scheme
├── js/
│   └── main.js                 # JavaScript functionality and animations
├── img/
│   ├── Falcon-motors.jpg       # Brand logo
│   ├── car-repair-maintenance-theme-mechanic-uniform-working-auto-service.jpg       # Carousel background
│   ├── carousel-bg-2.jpg       # Additional background
│   ├── service-*.jpg           # Service images
│   ├── team-*.jpg              # Team member photos
│   └── testimonial-*.jpg       # Testimonial photos
├── lib/                        # Third-party libraries
│   ├── animate/                # Animate.css
│   ├── counterup/              # Counter-Up plugin
│   ├── easing/                 # jQuery Easing
│   ├── owlcarousel/            # Owl Carousel
│   ├── tempusdominus/          # Date/Time picker
│   ├── waypoints/              # jQuery Waypoints
│   └── wow/                    # WOW.js
├── index.html                  # Homepage
├── about.html                  # About page
├── service.html                # Services page
├── booking.html                # Booking page
├── team.html                   # Team page
├── testimonial.html            # Testimonials page
├── contact.html                # Contact page
├── 404.html                    # 404 error page
└── README.md                   # This file
```

## Setup & Installation
1. Extract all files to your web server directory
2. Ensure all file paths are maintained (relative paths)
3. Open `index.html` in a web browser to view the website
4. For local development, use a local server (e.g., Python's `http.server` or Node's `http-server`)

## Running the Website Locally

### Using Python:
```bash
python -m http.server 8000
```
Then open `http://localhost:8000` in your browser.

### Using Node.js (http-server):
```bash
npm install -g http-server
http-server -p 8000
```

## Key Components & Styling

### Navigation Bar
- Dark background (#1A1A1A) for optimal contrast
- Light text that turns yellow on hover/active
- Sticky behavior: appears when scrolling past 300px
- Logo displayed with brand name

### Buttons
- Primary buttons: Yellow background with black text
- Hover state: Dark background with yellow text
- Secondary buttons: Maintain white text on dark background

### Service Navigation Pills
- Active state: Yellow background with black text
- Smooth transitions between states

### Team Member Cards
- Hover reveals yellow overlay with social media icons
- Dark icons on yellow overlay for visibility
- Icons turn yellow on dark background when hovered

### Testimonial Carousel
- Active testimonial features yellow background
- Black text on yellow for readability
- Automatic rotation with smooth transitions

### Booking Forms
- Yellow form containers with black text
- Date/time picker with yellow active dates
- Responsive layout for all screen sizes

## Browser Compatibility
- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Contact Information
- **General Inquiries:** info@falconmotors.com
- **Booking:** book@falconmotors.com
- **Technical Support:** tech@falconmotors.com
- **Address:** 123 Street, City, State ZIP
- **Phone:** +012 345 67890

## Copyright
© 2025 Falcon Motors. All Rights Reserved.

## Notes
- All animations are optimized for performance
- Images should be optimized for web use
- Logo file (`Falcon-motors.jpg`) must be present for proper display
- All third-party libraries are included in the `lib/` directory
- No server-side code required - pure static HTML/CSS/JavaScript

## Customization Tips
- Update contact information in all HTML files
- Replace placeholder images with actual photos
- Modify service descriptions and team member information
- Adjust color variables in `css/style.css` if needed (maintain accessibility)
- Update meta descriptions for SEO optimization

## License
Template designed by HTML Codex. Distributed by ThemeWagon.
Custom branding and modifications by Falcon Motors.

