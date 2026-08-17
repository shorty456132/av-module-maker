# UCI Customization

> Source: https://help.qsys.com/Content/Schematic_Library/uci_customization.htm

# UCI Customization

As User Control Interfaces (UCIs) are completely customizable, after adding a UCI to the design, you can then add controls, guidelines, images, navigation, layers, pages, graphics, and deploy your UCI design.

[Properties](javascript:void(0))

### User Control Interface Properties

To access the Properties for a UCI, you must select the UCI (not one of its pages) in the left-side pane under User Control Interfaces.

#### Title

User-defined name to uniquely identify the UCI. The Title does not display unless there is more than one Page for the UCI.

#### Style

Select a CSS style to apply to the UCI. See [UCI Styles](uci_styles.htm).

#### Panel Type

Select an iOS or TSC touch screen device, a generic aspect ratio, or a custom size.

[Custom](javascript:void(0))

Select an Orientation, Horizontal Resolution, and Vertical Resolution.

[Generic Aspect Ratio](javascript:void(0))

Select an aspect ratio and Orientation.

* Generic 16:10
* Generic 16:9
* Generic 4:3

[iPad and iPhone](javascript:void(0))

Select an iOS device model and Orientation.

* iPad
* iPad Mini
* iPad Pro 12.9, 10.5
* iPad Pro 9.7, Air 2
* iPhone
* iPhone 11 Pro, X, Xs
* iPhone 11, 11 Pro Max, Xs Max, Xr
* iPhone 5
* iPhone 6
* iPhone 6 Plus
* iPhone 8, 7, 6s
* iPhone 8+, 7+, 6s+

[Logitech Tap MTR](javascript:void(0))

The Logitech Tap is designed to work seamlessly with Microsoft Teams Room (MTR) systems, providing the appropriate formatting and functionality. Use it for any MTR based UCI.

[None](javascript:void(0))

Selecting the "None" option as the panel type allows a custom interface that is not assigned to any specific panel or device. This allows the UCI to be accessed and viewed on any compatible device or platform that supports Q-SYS UCIs, such as network PCs, tablets, or smartphones.

[TSC Touch Screen](javascript:void(0))

Select a QSC capacitive touch screen model and Orientation.

* TSC-101-G3
* TSC-116-G2
* TSC-47-G2
* TSC-50-G3
* TSC-55-G2
* TSC-7
* TSC-70-G3
* TSC-80-G2

#### Orientation

Set to the orientation of the screen used to display the UCI.

**Note:** When installing a touchscreen in portrait orientation, the Orientation property in the UCI Properties and the [Status/Control (Touch Screen)](touch_screen_status.htm) component must both be set to 'Portrait'.

#### Horizontal Resolution

Available only with the **Custom Panel Type**.

#### Vertical Resolution

Available only with the **Custom Panel Type**.

#### Tabs: Location

Available when there is more than one UCI page, and the Location Property is not "None".

Gives you the option to select the position of the tabs used for navigation between multiple pages. If there is only one page, there are no tabs.

**Note:** If you plan to use Tabs, add them prior to adding any controls. When you add Tabs, the usable area for placing controls changes.

#### Tabs: Style

Available when there is more than one UCI page, and the Location Property is not "None".

Gives you the option of Classic, or Chevron style tabs.

#### Tabs: Font Style

Available when there is more than one UCI page, and the Location Property is not "None".

Determines the style applied to the selected font. Available styles differ depending on the selected font.

#### Tabs: Font Size

Available when there is more than one UCI page, and the Location Property is not "None".

Controls the size of the font for the tabs as displayed on the UCI.

#### Tabs: Stroke Color

Available when there is more than one UCI page, and the Location Property is not "None".

Sets the color of the border between the tabs and UCI page.

#### Tabs: Stroke Width

Available when there is more than one UCI page, and the Location Property is not "None".

Sets the width of the border between the tabs and UCI page.

#### Swipe Disabled

Turns the Swipe function on the touchscreen on and off.

**Note:** This property only appears if the UCI contains multiple pages.

#### Private

Set this to Yes to hide this UCI from the iOS and Windows UCI viewers.

**Note:** When Private mode is enabled, you will still be able to view this UCI on Q-SYS touchscreen controllers, the HTML5 UCI viewer in Q-SYS Core Manager and Q-SYS Reflect, and within Q-SYS Designer.

#### Enable Button Swipe

Allows multiple buttons to be activated on a touch screen with a single, continuous finger swipe. As you swipe across multiple buttons, the buttons change state to match the state of the first button pressed. If disabled, each button must be pressed individually.

**Note:** This option is not applicable when controlling a UCI within Q-SYS Designer or the Q-SYS Control app on Apple iOS devices.

### Page Properties

Each page you add has its own Properties.

#### Title

To identify a UCI **Page**. Displays as a tab on the left side, and only when there is more than one page. In addition, you can change the Title by clicking the Page listed under the UCI in the **User Control Interfaces list**. Click the Page, then click directly on the Title to edit it.

#### Fill

Select the background color of each individual UCI page.

#### Icon

Select an icon image to appear next to the page tab text. If your UCI only uses one page, no icon is displayed.

### Control Properties

To change the properties of a control:

1. Select the control. The Properties for that control display in the right-side pane.
2. Change the Fill color, or any of the other Properties listed for the control. Depending on the style of control, different properties are available.

[Adding a UCI to the Design](javascript:void(0))

1. Select **User Control Interfaces** from the left-side pane.
2. Click  and select **New User Control Interface**.
3. Select the new UCI (for example, "Interface 1").
4. In the right-side pane, under Properties, configure the UCI as desired. See [User Control Interface Properties](#Web_Control_Interface_Properties).
5. In the middle pane, select **Page 1**.
6. In the right-side pane, under **Properties**, configure the UCI page, including its **Title**. See [Page Properties](#Page).
7. Add control elements to the UCI page to build your UCI. See [Adding Controls to a UCI Page](#Adding_Controls).
8. To add more pages, see [Working with Pages](#Working).
9. To configure layering within a page, see [Working with Layers](#Add_Layers).

[Adding Controls to a UCI Page](javascript:void(0))

There are two ways to add controls to a UCI:

[Add controls from the Schematic](javascript:void(0))

Use this method to copy controls from components in your schematic into a UCI. This is the traditional method of building a UCI.

To add controls to a UCI page:

1. Select the Page in the layout window to which you are going to add the controls.
2. Open the Control Panel for one of the Schematic Elements in your design.
3. Select one or more controls in the Control Panel
   * Click a single control
   * Click multiple controls using Ctrl+click
   * Use Ctrl+A to select all the controls in the Control Panel, including graphics. Make sure the Control Panel is selected before pressing Ctrl+A.
4. Once the desired controls are selected, drag, or copy and paste them into the UCI layout window. The controls you add to the UCI are directly linked to the controls in the component from which you selected them.
5. Modify control element properties and organize your design:
   * Select a control element to view its properties in the right-side pane. You can adjust an element's position, size, and other properties. For details, see [Control Properties](../Q-SYS_Designer/Using_the_Schematic/using_controls.htm#Control).
   * The Tools menu contains options for grouping elements, as well as aligning, distributing, packing, and ordering elements. For details, see [Grouping Schematic Elements](../Q-SYS_Designer/Using_the_Schematic/About_Schematic_Elements.htm#Grouping_Schematic_Elements) and [Aligning Schematic Elements](../Q-SYS_Designer/Using_the_Schematic/Labeling_and_Organizing_Schematic_Elements.htm#Aligning_Schematic_Elements).
   * Add guide lines to assist with element placement. See [Adding Guide Lines](#Guidelines).

[Add controls from the Toolbox](javascript:void(0))

Alternatively, you can use the User Control Interfaces > Toolbox tab to add, name, and link controls and then script the UCI in the UCI Script tab. This method is useful for UCI portability â i.e., you can easily copy and paste the UCI into a new UCI. The new UCI retains the script and component control links, and you can re-link individual controls or modify the script as desired.

To learn how to use this method, see the [UCI Controller](device_controller_proxy.htm)  topic.

### Limitations

* You must have at least one element of your design in the Schematic before you can add any controls or indicators to the UCI layout page. For more information about controls, see [Using Controls](../Q-SYS_Designer/Using_the_Schematic/using_controls.htm).
* The [Responsalyzer](responsalyzer.htm) and [RTA - Band-Pass](rta_bandpass.htm) components are the only components with a Response graph supported in a UCI.

[Adding Guide Lines](javascript:void(0))

When you open the UCI Design Interface, the working area is defined by a light blue background surrounded by gray area. If you place your cursor in the gray area above or to the left side of the working area, you will see a guide line displayed across or down through the workspace. The guide line moves with the cursor, and coordinates are displayed as you move the guide line.

* Double-click the cursor where you want the guide line to remain. Continue adding guide lines as needed.
* To move a guide line, move the cursor over the guide line in the gray area then click and hold when the cursor becomes a double arrow over the desired guide line. Drag the cursor to the place you want it. You can zoom in on the area if you need to in order to see the coordinates.
* To clear all guide lines, right-click in the gray area to the left or above the UCI area and click **Clear Guides**.
* After setting your guide lines, you can use them to align items in the UCI.

[Adding Images to a UCI Page](javascript:void(0))

You can add image files to a UCI in multiple ways.

**Note:** When you add graphics to a UCI, the images are scaled down for the Panel Type as set in the [User Control Interface Properties](#Web_Control_Interface_Properties). The images are never scaled up.

### Supported Image Types

You can add .png, .jpg, .jpeg, .gif, and .svg files to a UCI.

[Proper exporting of .svg files for a UCI](javascript:void(0))

For an .svg graphic to properly display in your UCI, ensure that you configure your graphics application to output an .svg file using the extents of the graphic itself instead of the "document" or "artboard" extents. For example:

* **Adobe Illustrator**: Export the Asset, not the Artboard.
* **Affinity Designer**: Select the "Selection with background" or "Selection without background" options. Do not select "Whole Document".
* **Figma**, **Sketch**: Select graphics for direct output as .svg.
* **Text editor**: When viewing .svg code in a text editor, the "viewBox=" property should reflect the actual extents of the graphic element, not the document extents.

**Note:** There is no visible difference between SVGs with height/width attributes and SVGs without these attributes when viewed on the UCI.

### Methods

* **Drag and drop**: You can drag and drop (or copy and paste) an image file onto the UCI canvas from another application. (Not all applications support both methods.). This is useful for adding a background and decorative graphics to your UCI.
* **As control button icon**: You can place a custom icon image over a control button. In the control's Graphic Properties, set the **Icon** property to "Custom". For more information, see [Control Presentation Properties](../Q-SYS_Designer/Using_the_Schematic/using_controls.htm#Control2).
* **As button image**: You can use an image as an entire control button (as opposed to an icon, which is an overlay). In the control's Graphic Properties, set the **Button Style** property to "Image". For more information, see [Control Presentation Properties](../Q-SYS_Designer/Using_the_Schematic/using_controls.htm#Control2).

[Adding Navigation to a UCI Page](javascript:void(0))

If you select **None** for the Tabs: Location property (see [User Control Interface Properties](#Web_Control_Interface_Properties)), you need to provide an alternate navigation method for the user. Q-SYS Designer provides two ways of adding navigation buttons to your UCI. In addition to the navigation type buttons, there are two control type buttons you can add. The Clean Screen button allows you to start a timer on a Q-SYS touchscreen (or in the UCI Viewer), which disables the display for 30 seconds to allow for cleaning. The Log Off Button will log off of the Q-SYS touchscreen if logging in is required.

**Note:** Although page transitions do not function in the Q-SYS Designer Software preview, they do function within the HTML5 viewer in Core Manager.

### Navigation Buttons

1. In the Schematic Library > UCI Buttons category, drag the Navigation Button into your UCI design.
2. With the button selected, select the UCI page you want in the Properties > Page. The Page property lists all of the Pages in your UCI.

You can alternatively add a navigation button by dragging a UCI page name into the editor for another UCI page:

1. In Design mode, select "Page 1". The page displays in the UCI design area.
2. In the left-side pane, drag the  icon for "Page 2" onto "Page 1" in the UCI design area. A button displays with the label "Page 2".
3. You can change the name by selecting the button and simply type a new name, or double-click the button and edit the name.
4. You can change various Properties of the button while it is selected.

### Polygon Buttons

1. In Design mode, select "Page 1". The page displays in the UCI design area.
2. Select the Polygon Graphic tool from the right-side pane.
3. Draw a polygon in the UCI design area.
4. In the left-side pane, drag the  icon for "Page 2" over the polygon on "Page 1". A hover message displays that says "Assign page to region".
5. Release the mouse button. The page you dragged on to the polygon button is now assigned to the polygon.

### Clean Screen Button

1. In Design mode, select the UCI page on which you wish to place the Clean Screen Button.
2. From the Schematic Library > UCI Buttons category, drag the Clean Screen Button into your UCI page.
3. When the design is run on a Q-SYS touchscreen controller (or in the UCI Viewer), this button starts the 30 second timer allowing you to clean the screen.

### Log Off Button

1. In Design mode, select the UCI page on which you wish to place the Log Off Button.
2. From the Schematic Library > UCI Buttons category, drag the Log Off Button into your UCI page.
3. Configure UCI access in Q-SYS Core Manager. See [User Control Interfaces](../Core_Manager/System_Management/User_Control_Interfaces.htm) in the Q-SYS Core Manager help.
4. When the design is run, this button logs the user off. You must enter a logon password to gain access.

### URL Button

1. In Design mode, select the UCI page on which you wish to place the URL Button.
2. From the Schematic Library > UCI Buttons category, drag the URL Button into your UCI page.
3. With the URL button selected, in the component Properties, enter the url you wish to connect to.
4. Run the design.
5. Make sure the device (UCI viewer, or iOS device) used for this UCI is running and connected to the UCI.
6. If necessary, select the page containing the URL button, and click the button.
7. The UCI opens your default browser and the url assigned to the button.

[Working with Pages](javascript:void(0))

### Adding, Deleting, and Re-ordering Pages

Use the toolbar at the bottom of the middle pane to manipulate UCI pages.

* Click  > **Add Page** to add a UCI page.
* Click  to delete the selected UCI pages.
* Click  or  to change the UCI page order.

### Copying and Pasting UCI Pages

* To copy or cut a UCI page, select the UCI page name in the middle pane, and then press Ctrl+C/Ctrl+X (or, select **Edit** > **Copy** or **Paste**.
* Select the destination UCI, and press Ctrl+V (or select **Edit** > **Paste**). The page now displays in the destination UCI.

[Working with Layers](javascript:void(0))

Think of Layers as stacked, transparent sheets of glass on which you can create images. You can see through the transparent areas of a layer to the layers below. You can work on each layer independently, experimenting to create the effect you want.

### Adding Layers

Adding layers to your UCI allows you to separate items on your UCI page. When you create a page in the UCI, it will always have at least one layer by default.

You can add a layer to a single page, or create a shared layer that can be used across multiple pages.

[Adding a Layer to a Page](javascript:void(0))

1. Select a page name.
2. Click  > **Add Layer** to add a layer to the selected page.
3. Add content to the layer â copy and paste or drag and drop items onto the selected layer.

[Adding Shared Layers](javascript:void(0))

You can create shared layers to easily share content between multiple pages. You add content to a shared layer the same as any other layer.

1. Click  > **Add Shared Layer**. The new shared layer is added at the Page level of the UI elements list.
2. Add content to the layer â copy and paste or drag and drop items onto the selected layer.
3. In the UI elements list, drag the shared layer name under the desired page names.

### Viewing, Ordering, and Deleting Layers

* To view the layers within a UCI page, click the drop-down arrow next to the page name.
* Click  or  to move a layer. Content on higher layers displays on top of the content on lower layers.
* Click  to delete the selected layers. You can delete a layer from the left pane regardless of its visibility or lock state.

### Hiding and Locking Layers and Layer Elements

* Click  to hide or show a layer or an element within a layer. The  icon indicates the layer or element is visible.

  [Notes](javascript:void(0))

  + When a layer is hidden you cannot select any content on that layer.
  + You can delete the layer and the content on the layer is also deleted.
* Click  to lock or unlock a layer or a layer element. The  icon indicates the layer is locked.

  [Notes](javascript:void(0))

  + You cannot add, delete, or move any content on a locked layer.
  + You can delete the layer when it is locked or unlocked.
* You can script actions of the layers. For more information, see [UCI](../Control_Scripting/Using_Lua_in_Q-Sys/Uci.htm).

[Adding Text and Graphics](javascript:void(0))

See [Graphic Tools](../Q-SYS_Designer/014_Graphic_Tools.htm).

[Adding CSS Styles to a UCI](javascript:void(0))

See [UCI Styles](uci_styles.htm).

[Deploying User Control Interfaces](javascript:void(0))

There are several ways you can display a UCI:

* On Q-SYS touchscreen controllers. See [Status/Control (Touch Screen)](touch_screen_status.htm).
* In the Q-SYS UCI Viewer for Windows. Download the Q-SYS UCI Viewer from the QSC website as part of the [Q-SYS software download](http://qsc.com/resources/software/q-sys-designer/).

  [Read more](javascript:void(0))

  + Install the Q-SYS UCI Viewer on the Windows PC that will be used to view the UCI. Follow the instructions in the installation program.
  + The [UCI Viewer Status/Control](uci_viewer.htm) component allows you to control various aspects and see the status of a UCI when a UCI Viewer client is associated with the UCI.
* On Apple iOS devices, including iPhone, iPhone 6, iPhone 6 Plus, iPad, and iPad Mini. Download the Q-SYS Control app from the App Store[.](https://itunes.apple.com/us/app/q-sys-control/id417461920?mt=8&ls=1 "Download Q-SYS App")

**Note:** Due to the finite amount of memory on any hardware, creating large UCIs can cause performance issues on the device hosting the UCI. Pay particular attention to smaller devices such as those that use the Apple iOS.
