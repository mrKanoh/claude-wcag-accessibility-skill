# Prompt: Generate alt text for images

Use when you need draft alt text for informative images. Always review before shipping.

---

## Prompt — informative image (copy & paste)

```
Write accessible alt text for the following image used in a [website / app / email].

Context:
- Page/section: [e.g. "Product page hero", "Blog post about typography"]
- Surrounding text: [Paste the text around the image so I can avoid redundancy]
- Purpose of the image: [Does it convey information, illustrate a concept, show a product, depict a person?]

Rules to follow:
1. Be concise (under 125 characters when possible) but complete
2. Do NOT start with "Image of" or "Photo of" — screen readers announce the image role
3. Do NOT repeat information already in surrounding text
4. If it's a chart/graph, describe the key finding, not visual style
5. If the image is decorative, return: alt=""

[DESCRIBE or attach the image]
```

---

## Prompt — complex image / infographic

```
Write a long description for the following complex image / infographic.

The alt attribute will be: alt="[SHORT TITLE]" with aria-describedby pointing to a hidden long description block.

Include:
- What type of visualization it is
- Key data points / trends / relationships
- Any labels, legends, or axes
- The main takeaway

[DESCRIBE or attach the image]
```

---

## Tips

- For SVG inline icons used purely decoratively: `aria-hidden="true" focusable="false"`
- For linked images: alt text = link destination ("Opens product page for Red Widget"), not image description
- Review AI-generated alt text — models sometimes hallucinate details
