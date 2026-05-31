# Rick Maxwell Portfolio - Image Optimization Plan

**Current Status**: 213.66 MB in `img/` assets + 1.59 MB of root image assets  
**Target**: ~15-20 MB total image payload after optimization  
**Expected Benefit**: faster page loads, improved SEO, better mobile experience

---

## Completed Work

### PSD Files Removed ✅
- No `.psd` files remain in the production image tree.
- This eliminated the largest unnecessary source asset class from the site.

### Hero Image Optimization ✅
- `homeImage-2.webp` and `homeImage-2-opt.jpg` now exist at the project root.
- `index.html` already uses a `<picture>` block with WebP fallback and `loading="lazy"`.
- Hero payload is now approximately `0.15 MB` for WebP and `0.24 MB` for optimized JPEG.

### WebP Conversion Started ✅
- `197` WebP files are present in `img/`.
- The script `optimize_homeImage2.py` generates WebP and optimized `-opt.jpg` versions for supported source images.
- `index.html` already uses WebP `<source>` elements for the 2023-2026 portfolio section.

### Format Consistency ✅
- No `.jpeg` files remain in the image tree.
- All JPEG assets are now standardized as `.jpg`.

### Lazy Loading Implemented ✅
- Portfolio images already include `loading="lazy"` in HTML.
- This reduces initial page load work and defers offscreen image downloads.

---

## Current Image Inventory
- `.jpg`: 276 files
- `.png`: 13 files
- `.webp`: 197 files
- `.psd`: 0 files
- Total size in `img/`: 213.66 MB
- Total root image assets: 1.59 MB

---

## Remaining Work

### 1. Confirm full WebP coverage across all portfolio sections
- The 2023-2026 section is already using WebP sources.
- Audit the remaining sections and add `<source srcset="*.webp" type="image/webp">` where missing.

### 2. Create mobile-specific responsive image variants
- Build `-mobile.webp` / `-mobile.jpg` files for the largest hero and portfolio images.
- Use max widths around `600-800px` for phone displays.

### 3. Reduce remaining large JPGs
- Target the current high-size images in `img/2023-2026/`, `img/2020-2022/`, and `img/2017-2019/`.
- Use the existing script or batch tools to resize and recompress these images.

### 4. Optimize PNGs where appropriate
- Evaluate the `13` PNG files and convert those that do not need transparency to WebP.

---

## Recommended Next Steps

1. Use `optimize_homeImage2.py` or a similar batch script to generate WebP and optimized JPEG variants for all supported images.
2. Update any remaining HTML image references to use WebP sources first, with JPEG fallback.
3. Add mobile `srcset` variants in the hero and key portfolio image blocks.
4. Re-run a size audit after the next batch of conversions to verify progress.

---

## Practical Goal
- Move from the current `~215 MB` of image assets toward a final served payload of `15-20 MB`.
- With the current cleanup and WebP progress, the remaining work is mostly HTML coverage and selective recompression, not new tooling.

---

## Notes
- The current site is no longer in the initial “raw asset” state: the core optimization infrastructure is in place.
- Focus now on extending the WebP/responsive pattern site-wide and trimming the largest remaining JPGs.

- Update all img tags with `<picture>` elements
- Add responsive breakpoints
- **Time**: 4 hours | **Result**: Complete responsiveness

### Phase 5: Testing & Validation (Week 3)
- Test on mobile/tablet/desktop
- Verify image quality
- Check browser compatibility
- **Time**: 2 hours

**Total Implementation Time**: ~12 hours  
**Total Savings**: 87-91% reduction (142 MB → 15-20 MB)

---

## Tools & Resources

### Free Tools:
- **ImageMagick**: Batch image processing
  ```
  https://imagemagick.org/
  choco install imagemagick (Windows)
  ```
- **cwebp**: WebP conversion (Google)
  ```
  https://developers.google.com/speed/webp/download
  ```
- **FFmpeg**: Video/image batch processing
- **GIMP**: Manual editing if needed

### Paid Services (Optional):
- **TinyJPG API**: $0.002 per image (best for batches)
- **ImageOptim Pro**: $39 one-time
- **Cloudflare Image Optimization**: Free with CDN

### Online Tools (No Installation):
- https://imageoptim.com/online
- https://tinyjpg.com/
- https://convertio.co/jpg-webp/

---

## Success Metrics

| Metric | Before | After | Goal |
|--------|--------|-------|------|
| Total Image Size | 142 MB | 15-20 MB | ✅ |
| Hero Image | 1.2 MB | 150 KB | ✅ |
| Avg Portfolio Image | 2 MB | 300 KB | ✅ |
| Page Load Time | ~8-12s | ~1-2s | ✅ |
| Mobile Experience | Poor | Excellent | ✅ |
| SEO Score | ~70 | ~95+ | ✅ |
| Lighthouse Performance | ~55 | ~90+ | ✅ |

---

## Notes & Recommendations

1. **Backup First**: Keep originals in an archive folder
2. **Quality Verification**: Spot-check 5-10 images after compression
3. **Version Control**: Commit changes incrementally
4. **Monitor**: Use Google PageSpeed Insights before/after
5. **Future Workflow**: 
   - Export from camera/Lightroom at 70% quality, 1500px max
   - Use WebP as primary format
   - Create mobile variants automatically

