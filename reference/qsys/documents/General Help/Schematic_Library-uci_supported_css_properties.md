# Supported CSS Properties

> Source: https://help.qsys.com/Content/Schematic_Library/uci_supported_css_properties.htm

# Supported CSS Properties

The following tables indicates the available properties and selectors that are supported for specific UCI graphic and control elements.

= Supported

Using a supported CSS Property, you can install custom Cascading Style Sheet (.css) files to a design, and then apply a selected style to a user control interface (UCI). Visit [Style Reference](uci_styles.htm#Style_Ref) to learn more.

### Graphics

| Property | Page | Textblock | Groupbox | Header | Image | Polygon | Flexbox |
| --- | --- | --- | --- | --- | --- | --- | --- |
| align-content |  |  |  |  |  |  |  |
| align-items |  |  |  |  |  |  |  |
| background |  |  |  |  |  |  |  |
| background-color |  |  |  |  |  |  |  |
| background-image[4](#Only7) |  |  |  |  |  |  |  |
| background-position |  |  |  |  |  |  |  |
| background-size |  |  |  |  |  |  |  |
| border[5](#Supports) |  |  | [1](#Only) |  |  | [1](#Only) | [1](#Only) |
| border-width |  |  | [1](#Only) |  |  | [1](#Only) | [1](#Only) |
| border-\* |  |  | [1](#Only) |  |  | [1](#Only) | [1](#Only) |
| border-\*-width[5](#Supports) |  |  | [1](#Only) |  |  | [1](#Only) | [1](#Only) |
| border-\*-color |  |  | [1](#Only) |  |  | [1](#Only) | [1](#Only) |
| border-radius |  |  | [2](#Only2) |  |  |  | [2](#Only2) |
| color |  |  |  |  |  |  |  |
| content |  |  |  |  |  |  |  |
| flex-direction |  |  |  |  |  |  |  |
| flex-wrap |  |  |  |  |  |  |  |
| font-family[6](#Q-SYS2) |  |  |  |  |  |  |  |
| font-size[5](#Supports) |  |  |  |  |  |  |  |
| gap |  |  |  |  |  |  |  |
| justify-content |  |  |  |  |  |  |  |
| margin |  |  |  |  |  |  |  |
| opacity |  |  |  |  |  |  |  |
| padding |  |  |  |  |  |  |  |
| text-align |  |  |  |  |  |  |  |
| text-transform |  |  |  |  |  |  |  |
| vertical-align |  |  |  |  |  |  |  |
| -qsc-font-style[3](#Specific) |  |  |  |  |  |  |  |

###### 1. Only supports single border color and thickness (uses left).

###### 2. Only supports single corner radius (uses top left).

###### 3. Specific to QSC, and uses the same values as the Font Style property drop-down â Bold, Italic, Bold Italic, etc.

###### 4. Only supports `url()` and `linear-gradient()` background-images.

###### 5. Supports size in pixels (px). Also supports viewport relative sizes. See [Setting viewport relative sizes](uci_styles.htm#Setting) for example usage.

###### 6. Q-SYS does not support CSS Font Fallbacks. Define only a single font for the font-family property.

### Controls

| Property | Button | Textbox | Knob | LED | Fader | Meter | Combobox | Listbox |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| background |  |  | [1](#Only3) |  | [1](#Only3) |  |  |  |
| background-color |  |  |  |  |  |  |  |  |
| background-image[4](#Only6) |  |  |  |  |  |  |  |  |
| background-position |  |  |  |  |  |  |  |  |
| background-size |  |  |  |  |  |  |  |  |
| border[5](#Supports2) |  |  |  |  | [2](#Only4) |  |  |  |
| border-width |  |  |  |  | [2](#Only4) |  |  |  |
| border-\* |  |  |  |  | [2](#Only4) |  |  |  |
| border-\*-width[5](#Supports2) |  |  |  |  | [2](#Only4) |  |  |  |
| border-\*-color |  |  |  |  | [2](#Only4) |  |  |  |
| border-radius |  |  |  |  | [3](#Only5) |  |  |  |
| color |  |  |  |  |  |  |  |  |
| content |  |  |  |  |  |  |  |  |
| font-family[8](#Q-SYS) |  |  |  |  |  |  |  |  |
| font-size[5](#Supports2) |  |  |  |  |  |  |  |  |
| margin |  |  |  |  |  |  |  |  |
| opacity |  |  |  |  |  |  |  |  |
| padding |  |  |  |  |  |  |  |  |
| text-align |  |  |  |  |  |  |  |  |
| text-transform |  |  |  |  |  |  |  |  |
| vertical-align |  |  |  |  |  |  |  |  |
| -qsc-font-style |  |  |  |  |  |  |  |  |
| -qsc-icon[6](#Refer) |  |  |  |  |  |  |  |  |
| -qsc-icon-color[6](#Refer) |  |  |  |  |  |  |  |  |
| -qsc-icon-font[6](#Refer) |  |  |  |  |  |  |  |  |
| -qsc-icon-align[6](#Refer) |  |  |  |  |  |  |  |  |
| -qsc-render-style[7](#Refer2) |  |  |  |  |  |  |  |  |

###### 1. Only supports color (not images) on the background.

###### 2. Only supports single border color and thickness (uses left).

###### 3. Only supports single corner radius (uses top left).

###### 4. Only supports `url()` and `linear-gradient()` background-images.

###### 5. Supports size in pixels (px). Also supports viewport relative sizes. See [Setting viewport relative sizes](uci_styles.htm#Setting) for example usage.

###### 6. See [Referencing icon fonts](uci_styles.htm#Referenc3) for details and examples.

###### 7. See [Rendering Styles for Meters, Knobs, and Faders](uci_styles.htm#Renderin) for details and examples.

###### 8. Q-SYS does not support CSS Font Fallbacks. Define only a single font for the font-family property.
