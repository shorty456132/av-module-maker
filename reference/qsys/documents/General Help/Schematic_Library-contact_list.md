# Contact List

> Source: https://help.qsys.com/Content/Schematic_Library/contact_list.htm

# Contact List

The Contact List component allows you to access contact lists that have been set up in [Core Manager](../Core_Manager/CoreManager_Overview.htm). After selecting a Contact List, you can select or search for the contact you want to call. To dial a selected number, expose the Number control pin and wire it to the Call Control > Dial String control pin of the [Status/Control (Softphone)](Softphone.htm).

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Example](javascript:void(0))

In this example, we have exposed the Number Control Pin on the Contact List as well as the Control Dial Control Pin on the Status Softphone component. With the connection made between them, we can create a UCI that will dial specific contacts at the press of a button.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Contact List Properties

There are no configurable properties for this component.

[Controls](javascript:void(0))

#### Contact Lists

When a Contact List is established in the Q-SYS Core Manager > [Telephony > Contacts](../Core_Manager/System_Management/Contacts.htm) page, it displays in this field. A contact list is comprised of one or more contacts.

#### Search

Searches in the selected Contact List.

Select the search field and type the name for which you want to search. All items meeting the criteria display. Items not meeting the criteria are not displayed.

#### Names

The names of the Contacts in the selected Contact List.

#### Number

Displays the number associated with the selected Contact.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| List  (Selected Contact List) | â | Text | â | Input / Output |
| Names  (Selected Name) | â | Text | â | Input / Output |
| Number  (Number of Selected Name) | â | Text | â | Output |
| Search  (String typed in Search field after Dial is clicked) | â | Text | â | Input / Output |
