
from pxr import Usd
# Create a stage that lives in memory
stage = Usd.Stage.CreateInMemory()
worldPrim = stage.DefinePrim("/World")
# Add an attribute called 'Bar' and the value 'Bar'
fooAttr = worldPrim.GetAttributes().CreateAttribute("Bar", Sdf.ValueTypeName.String)
fooAttr.Set("Bar")
stage.ExportToString()