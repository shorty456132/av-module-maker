# Search and Replace

> Source: https://help.qsys.com/Content/Q-Sys_Designer/search_and_replace.htm

# Search and Replace

Search and Replace allows you to search for specific text and then replace it with different text. You can replace all text at once, or choose specific text to replace. You can search for inventory names, schematic pages, blocks, labels, code names, pin names, names of UCIs, elements within UCIs, and UCI Toolbox Controls. This feature is beneficial when using design templates or duplicating programming in larger designs.

To use the **Search and Replace** feature, open a design in Q-SYS Designer and press the **Ctrl + H** buttons, or select **Edit** > **Search and Replace** from the main menu.

[Using the Search](javascript:void(0))

1. Press the **Ctrl + H** buttons, or select **Edit** > **Search and Replace** from the main menu.
2. The **Search and Replace** dialog box will appear.
3. In the **Search** field, type the text as it appears within the design.

### Advanced Search Options

You can specify the **Search** feature to *Match case*, *Match whole word*, or *Use regular expressions*. You can also search *Everywhere*, or in a *Selection*.

**Note:** Be sure to choose an area before pressing **Ctrl + H** buttons, or select **Edit** > **Search and Replace** from the main menu.

### Using Regular Expressions

In cases where multiple inventory items are added that are the same, you can use the Search and Replace feature to rename them using the *Use regular expressions* option. Additionally, you can use the feature to correct any misspelling or change nomenclature across the entire design.

[Example 1: Multiple Inventory Items](javascript:void(0)) 

In the example below, we have added three TSC-70-G3 to our design and we are using the Search and Replace feature to rename them all at once in sequential order.

**Note:** Use `(\d)` to represent the digit range 0-9 and `$1` to match the substring that is to be replaced.

[Example 2: Changing Nomenclature](javascript:void(0))

In this design, we have a mixer that has used the nomenclature "Wireless 1-n", "Wirless 1-n", and "RF 1-n". To easily correct it, we can utilize the *Use regular expressions* option to find and replace our text.

**Note:** When looking for multiple words, separate them by the pipe ( | ) symbol.

[Using the Replace](javascript:void(0))

1. After typing your text in the **Search** field, items with the same name will appear in the **Results Field** dialog box.
2. In the **Replace** field, type the text you want to replace it with.

### Advanced Replace Options

You will be given the opportunity to replace everything (represented by check-marks) or you can choose which items to be replaced by removing the check-marks. Once you have made your selection, click on the **Replace Button**.
