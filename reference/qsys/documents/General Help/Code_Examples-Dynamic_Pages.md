# Dynamic Pages

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/Dynamic_Pages.htm

# Dynamic Pages

Dynamic pages can be useful for optional features, model specific controls, or a dedicated debug page. This example demonstrates showing dynamic pages in a plugin via properties.

## Breakdown

One way to achieve this is by defining a function to modify the page name table and call that function at the beginning of your design time functions. In this case, we define GetDynamicPages(props) at the top of our plugin, and then call it in GetPages() and GetLayout().

Note that the page tabs won't show until there are more than 2 pages returned by GetPages(). Also, pages are in the order shown in the returned table. This matters, since the first page is the page a user would initially see when opening up the plugin within QDS.

## The Code

```lua
PluginInfo = {  
    Name = "Examples~Dynamic Pages",  
    Version = "0.0",  
    BuildVersion = "0.0.1.0",  
    Id = "e3b46ecb-d317-4ebd-8f3f-9870fb30f0d9",  
    Description = "An example plugin that demonstrates how to create dynamic pages.",  
}  
  
function GetDynamicPages(props)  
  if props["Enable Page 2"].Value then  
    table.insert(pagenames,"Page 2")  
  end  
  if props["Enable Page 3"].Value then  
    table.insert(pagenames,"Page 3")  
  end  
end  
  
function GetColor(props)  
  return { 102, 102, 102 }  
end  
  
function GetPrettyName(props)  
  return "Dynamic Pages " .. PluginInfo.BuildVersion  
end  
  
pagenames = {"Main"}  
  
function GetPages(props)  
  local pages = {}  
  GetDynamicPages(props)  
  for ix,name in ipairs(pagenames) do  
    table.insert(pages,{name = pagenames[ix]})  
  end  
  return pages  
end  
  
function GetProperties()  
  local props = {}  
  table.insert(props,{  
    Name = "Enable Page 2",  
    Type = "boolean",  
    Value = false})  
  table.insert(props,{  
    Name = "Enable Page 3",  
    Type = "boolean",  
    Value = false})  
  return props  
end  
  
function RectifyProperties(props)  
  return props  
end  
  
function GetControls(props)  
  local controls = {}  
  return controls  
end  
  
function GetControlLayout(props)  
  local layout   = {}  
  local graphics = {}  
  GetDynamicPages(props)  
  local CurrentPage = pagenames[props["page_index"].Value]  
    
  if CurrentPage == "Main" then  
    table.insert(  
      graphics,  
      {  
        Type = "GroupBox",  
        Text = "Main Page",  
        Position = {0, 0},  
        Size = {200, 100},  
        StrokeWidth = 1,  
        StrokeColor = {51, 51, 51},  
        CornerRadius = 8,  
        FontSize = 14,  
        HTextAlign = "Left"  
      }  
    )  
  elseif CurrentPage == "Page 2" then  
    table.insert(  
      graphics,  
      {  
        Type = "GroupBox",  
        Text = "Page 2",  
        Position = {0, 0},  
        Size = {200, 100},  
        StrokeWidth = 1,  
        StrokeColor = {51, 51, 51},  
        CornerRadius = 8,  
        FontSize = 14,  
        HTextAlign = "Left"  
      }  
    )  
  elseif CurrentPage == "Page 3" then  
    table.insert(  
      graphics,  
      {  
        Type = "GroupBox",  
        Text = "Page 3",  
        Position = {0, 0},  
        Size = {200, 100},  
        StrokeWidth = 1,  
        StrokeColor = {51, 51, 51},  
        CornerRadius = 8,  
        FontSize = 14,  
        HTextAlign = "Left"  
      }  
    )  
  end  
  return layout, graphics  
end  
  
--Start event based logic  
if Controls then  
end
```
