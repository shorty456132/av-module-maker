# Styles_CSS_Example

> Source: https://help.qsys.com/Content/Resources/MicroContent/Styles_CSS_Example.htm

```lua
/***********CSS Format for low/unpressed state********************
.<CSS_ClassName>{					//Class name referenced in the CSS Class Name property for the UI element in Designer
	<CSS_Selector1>:<SelectorValue/String>;
	<CSS_Selector2>:<SelectorValue/String>
}

/***********CSS Format for low/unpressed state********************
.<CSS_ClassName>:value(1){
	<CSS_Selector1>:<SelectorValue/String>;
	<CSS_Selector2>:<SelectorValue/String>
}
*/



/******Text Block properties for the CSS Status file link*******/

.CSSStatus{
	content: "Has Been Established"  
}



/***********Text properties for the Gain Component*************/

.GainText{
	color: rgba(255,255,255,1.0); 
	font-size: 24;
	border-radius: 8; 
	background-color: rgba(100,100,100,1.0);  
}



/***********Controls properties for the Gain Component*************/

.GainBypassButton{
    	background-color: rgba(40,100,100,1.0);  
}
 
.GainBypassButton:value(1) {
    	background-color: rgba(0,200,200,1.0); 
}

.GainInvertButton{
    	background-color: rgba(100,100,30,1.0);  
}
 
.GainInvertButton:value(1) {
    	background-color: rgba(255,255,30,1.0); 
}

.GainMuteButton{
    	background-color: rgba(100,40,40,1.0);  
}
 
.GainMuteButton:value(1) {
    	background-color: rgba(255,40,40,1.0); 
}

.GainLevelKnob{
    	background-color: rgba(175,175,40,1.0);  
}

.GainLevelFader{
	border-width: 3;	
	border-left-color: rgba(80,80,80,1.0);
    	background-color: rgba(150,150,190,1.0);  
}




/***********Text properties for the Router Component*************/

.RouterText{
	color: rgba(0,0,0,1.0); 
	font-size: 24;
	border-radius: 12; 
	background-color: rgba(175,175,175,1.0);
	text-align: center  
}



/***********Controls properties for the Router Component*************/

.RouterButton{
    	background-color: rgba(40,40,40,1.0); 
	border-left-color: rgba(125,125,125,1.0);
	border-right-color: rgba(125,125,125,1.0);
	border-top-color: rgba(255,255,255,1.0);
	border-bottom-color: rgba(255,255,255,1.0);
	border-width: 4;
	content: "Off";
	font-size: 16
}
 
.RouterButton:value(1) {
    	background-color: rgba(125,255,125,1.0);
	border-left-color: rgba(255,255,125,1.0);
	border-right-color: rgba(255,255,125,1.0);
	border-top-color: rgba(125,125,125,1.0);
	border-bottom-color: rgba(125,125,125,1.0);
	border-width: 4;
	content: "On";
	font-size: 24 
}



/***********Text Box properties for the QSC Logo image*************/
/***********Logo image file must be in the same folder as CSS file***/
.TextBlock {
    	background-image: url(QSC_Logo.png);
}



/***********Group Box properties***********************************/
.GroupBox {
	font-family: Adamina;
	text-align: center;
}
```
