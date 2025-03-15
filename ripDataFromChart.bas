Attribute VB_Name = "Module1"
Sub RipChartValues()

Dim cht As PowerPoint.Chart
Dim seriesIndex As Long
Dim labels As Variant
Dim values As Variant
Dim name As String
Dim buffer As String
Dim objData As Object

Set cht = ActiveWindow.Selection.ShapeRange.Parent.Shapes(ActiveWindow.Selection.ShapeRange.name).Chart

With cht
    For seriesIndex = 1 To .SeriesCollection.Count
    name = .SeriesCollection(seriesIndex).name
    labels = .SeriesCollection(seriesIndex).XValues
    values = .SeriesCollection(seriesIndex).values

    If seriesIndex = 1 Then buffer = vbTab & Join(labels, vbTab) & vbCrLf
    buffer = buffer & (name & vbTab & Join(values, vbTab) & vbCrLf)
    Next

End With

On Error Resume Next
' Rory's late bind example
' this is a late bound MSForms.DataObject
Set objData = CreateObject("New:{1C3B4210-F441-11CE-B9EA-00AA006B1A69}")

' copy current cell formula to clipboard
With objData
    .SetText buffer
    .PutInClipboard
    MsgBox "Data extracted to clipboard!", vbOKOnly, "Success"
End With

End Sub
