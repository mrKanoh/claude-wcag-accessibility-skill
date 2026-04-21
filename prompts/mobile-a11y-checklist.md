# Prompt: Mobile accessibility checklist

Use when building or auditing a native mobile app (React Native, SwiftUI, or
Jetpack Compose) and you want a platform-specific accessibility checklist and fix guidance.

---

## Prompt (copy & paste)

```
Generate a complete mobile accessibility checklist and audit for the following:

**Platform:** [React Native / SwiftUI (iOS) / Jetpack Compose (Android)]
**Component/screen:** [e.g., "Login screen", "Settings page", "Chat message list"]
**Paste code or describe the UI:**
[CODE OR DESCRIPTION]

For each platform, check:

### React Native
- [ ] All touchable elements have `accessibilityLabel` (replaces visual text for screen readers)
- [ ] `accessibilityHint` for non-obvious interactions ("double-tap to open details")
- [ ] `accessibilityRole` set correctly (button, link, image, header, checkbox, etc.)
- [ ] `accessibilityState` for toggle states ({ checked: true }, { disabled: true })
- [ ] `accessible={true}` on grouped elements (combine label + value into one focus target)
- [ ] `importantForAccessibility="no"` on decorative views
- [ ] `accessibilityLiveRegion` for dynamic content updates ("polite" or "assertive")
- [ ] Touch targets >= 44x44 pt (use minHeight/minWidth on StyleSheet)
- [ ] Text scales with Dynamic Type (avoid fixed font sizes — use sp units via PixelRatio)
- [ ] `reduceMotionEnabled` check: `AccessibilityInfo.isReduceMotionEnabled()`
- [ ] Keyboard/Switch Access: all interactive elements reachable without touch
- [ ] Focus management on screen transitions: `AccessibilityInfo.setAccessibilityFocus(ref)`
- [ ] ScrollViews: `accessibilityScrollable={true}`

### SwiftUI (iOS VoiceOver)
- [ ] `.accessibilityLabel("descriptive text")` on all interactive views
- [ ] `.accessibilityHint("double tap to...")` for non-obvious interactions
- [ ] `.accessibilityTraits([.isButton, .isHeader, .isLink, .isImage])` set correctly
- [ ] `.accessibilityValue("on")` for toggle/slider current values
- [ ] `.accessibilityHidden(true)` for decorative elements
- [ ] `.accessibilityElement(children: .combine)` for grouped elements
- [ ] `.accessibilityAddTraits(.isSelected)` for selected states
- [ ] Dynamic Type: `.font(.body)` (system fonts scale) not `.font(.system(size: 16))`
- [ ] Minimum tap target: `.frame(minWidth: 44, minHeight: 44)` or `.contentShape(Rectangle())`
- [ ] Reduce Motion: `@Environment(\.accessibilityReduceMotion) var reduceMotion`
- [ ] Focus order: `.accessibilitySortPriority(N)` when SwiftUI order is wrong
- [ ] Announcement on state change: `UIAccessibility.post(notification: .announcement, argument: "Saved")`

### Jetpack Compose (Android TalkBack)
- [ ] `Modifier.semantics { contentDescription = "..." }` on all interactive composables
- [ ] `Modifier.semantics { role = Role.Button }` for correct role
- [ ] `Modifier.semantics { stateDescription = "checked" }` for toggle states
- [ ] `Modifier.semantics { heading() }` for headings
- [ ] `Modifier.semantics { invisibleToUser() }` for decorative elements
- [ ] `Modifier.clearAndSetSemantics { ... }` to override child semantics
- [ ] Touch target: `Modifier.minimumInteractiveComponentSize()` (48dp Compose default)
- [ ] Dynamic font: `MaterialTheme.typography.bodyLarge` (scales with system)
- [ ] Reduce Motion: `LocalReduceMotion.current` (custom) or check `AnimationController`
- [ ] Focus management: `FocusRequester` + `LaunchedEffect` for screen transitions
- [ ] Live regions: `Modifier.semantics { liveRegion = LiveRegionMode.Polite }`
- [ ] Keyboard/hardware input: `Modifier.focusable()` + `onKeyEvent`

For each issue found provide:
1. The specific composable/modifier/property missing
2. A before/after code snippet
3. The WCAG SC equivalent (mobile a11y maps to same criteria)
4. How to test it (TalkBack gesture / VoiceOver gesture / Switch Access)
```

---

## Tips

- Test React Native with: VoiceOver (iOS) + TalkBack (Android)
- Use Xcode Accessibility Inspector for SwiftUI static analysis
- Use Android Studio Accessibility Scanner for Compose
- Check `data/screen-reader-keys.csv` for TalkBack and VoiceOver gestures
