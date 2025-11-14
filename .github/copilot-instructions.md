# Restaurante Website - Copilot Instructions

## Project Overview
Static restaurant website built with vanilla HTML, CSS, and JavaScript. Multi-page site with responsive design using custom CSS grid/flexbox system. Backend contact form processing via PHP mail function.

## Architecture & Key Components

### Page Structure
- **Single Header Template**: All pages (`index.html`, `contacto.html`, `nosotros.html`, `galeria.html`) replicate the same header with logo and contact info
- **Responsive Navigation**: Mobile hamburger menu (`.icon-menu`) toggling `.menu` visibility via `menu.js`
- **Unified Footer**: Consistent footer styling across pages
- **Page-Specific CSS**: Each page has its own stylesheet (e.g., `contacto.css`, `galeria.css`) alongside shared `estilos.css`

### CSS Architecture
- **Utility-First Approach**: Classes like `.column`, `.column--50`, `.column--50-25` define layout using `width` percentages
- **Container Pattern**: `.container--flex` uses flexbox with `flex-wrap: wrap` and `justify-content: space-between` for responsive layouts
- **BEM-Like Naming**: Modified BEM pattern (e.g., `.main-header__contactInfo__phone`, `.today-special__title`)
- **Key Responsive Units**: Montserrat font (400, 700 weight) and Pacifico script font for branding
- **Color Scheme**: Primary red `#DE423A` used for branding, white/neutral accents

### JavaScript Interactivity
- **`menu.js`**: Toggles `.mostrar` class on `#menu` element when hamburger icon clicked
- **`modal.js`**: Gallery image modal - clicking gallery images toggles `.modal--open` class, dynamically sets modal image `src` attribute
- **Event Pattern**: Simple `addEventListener('click')` with `classList.toggle()` for state management

### Backend Integration
- **Contact Form**: `contacto.html` form (POST to `enviar.php`) collects name, email, phone, message
- **PHP Handler** (`enviar.php`): Uses native `mail()` function to send to hardcoded recipient (`argofrogg@gmail.com`), redirects to `index.html`
- **No Validation**: Form relies on HTML5 `required` attributes only

## Development Conventions

### When Adding New Pages
1. Copy header/nav/footer structure from existing pages
2. Create page-specific CSS file in `css/` directory (import in page `<head>`)
3. Link new page in navigation menu across ALL pages (not currently automated)
4. Use responsive column classes (`.column--50`, `.column--25`, etc.) for layouts

### When Modifying Styles
- Edit shared `estilos.css` for global changes (header, nav, footer, container utilities)
- Edit page-specific CSS files for unique section styling
- Maintain `.column--{width}` naming convention for layout classes
- Always use flexbox/grid utility classes, avoid inline styles

### Contact Form Updates
- Form fields in `contacto.html` must have `name` attributes matching `$_POST` keys in `enviar.php`
- Update recipient email by changing `$destino` variable in `enviar.php`
- All form processing is synchronous with page redirect (no AJAX)

### Mobile Responsiveness
- Viewport meta tag: `width=device-width, initial-scale=1.0, maximum-scale=3.0`
- Mobile menu triggered via `.icon-menu` element (hamburger icon)
- Icons from external FontAwesome-like service: `https://file.myfontastic.com/pJA6HqcXAaBqwGLcfFYXuj/icons.css`
- Test responsive behavior by toggling menu display and verifying flex layouts adapt to narrow viewports

## Critical Files Reference
- **Layout Foundation**: `css/estilos.css` (403 lines) - base styles, header, nav, container/column utilities
- **Menu Toggle**: `js/menu.js` - controls mobile hamburger menu
- **Gallery Modal**: `js/modal.js` - manages image lightbox functionality
- **Contact Processing**: `enviar.php` - email handler with hardcoded recipient
- **HTML Templates**: Replicable structure across all `.html` files

## Integration Points
- **External Dependencies**: Google Fonts (Montserrat, Pacifico), custom icon font service
- **Email Service**: PHP `mail()` function (requires server-side SMTP configuration)
- **No Framework**: Vanilla DOM manipulation using `getElementById`, `querySelector`, `classList.toggle()`

## Known Patterns & Quirks
- Header/nav markup duplicated across pages (consider refactoring with template system)
- Contact form email hardcoded in `enviar.php` (not configurable via environment variables)
- Modal uses `id` selectors; image gallery assumes specific HTML structure (`.gallery__img` class)
- CSS column widths not responsive via media queries; relies on flexbox wrapping instead
