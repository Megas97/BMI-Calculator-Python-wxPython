import wx
import time

class BMICalculator(wx.Frame):
	def __init__(self, parent, id):
		wx.Frame.__init__(self, parent, id, "BMI Calculator", (600, 800))
		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour("#FFFFFF")
		self.Centre()
		self.info_text = wx.StaticText(self.panel, -1, "Enter your height and weight and press compute to see your BMI.", (20, 15))
		self.label_text = wx.StaticText(self.panel, -1, "Body Mass Index: ", (20, 50))
		self.result_text = wx.StaticText(self.panel, -1, "... kg/(m*m)", (120, 50))
		self.error_label = wx.StaticText(self.panel, -1, "Error(s): ", (290, 50))
		self.error_text = wx.StaticText(self.panel, -1, "", (269, 65))
		self.static_text_height = wx.StaticText(self.panel, -1, "Height:", (20, 90))
		self.height = wx.SpinCtrlDouble(self.panel, -1, pos = (65, 87), size = (60, -1), min = 0, max = 300)
		self.static_text_height_extra = wx.StaticText(self.panel, -1, "(in centimeters)", (130, 90))
		self.static_text_weight = wx.StaticText(self.panel, -1, "Weight:", (20, 130))
		self.weight = wx.SpinCtrlDouble(self.panel, -1, pos = (65, 127), size = (60, -1), min = 0, max = 300)
		self.static_text_weight_extra = wx.StaticText(self.panel, -1, "(in kilograms)", (130, 130))
		self.bmi_underweight = wx.StaticText(self.panel, -1, "Underweight = < 18.5", (253, 90))
		self.bmi_normal_weight = wx.StaticText(self.panel, -1, "Normal weight = 18.5-24.9", (239, 110))
		self.bmi_overweight = wx.StaticText(self.panel, -1, "Overweight = 25-29.9", (254, 130))
		self.bmi_obesity = wx.StaticText(self.panel, -1, "Obesity = > 30", (274, 150))
		self.button_compute = wx.Button(self.panel, label = "Compute", pos = (40, 170), size = (60, -1))
		self.button_compute.SetBackgroundColour((0, 255, 0))
		self.button_compute.Bind(wx.EVT_BUTTON, self.onCompute)
		self.button_refresh = wx.Button(self.panel, label = "Refresh", pos = (122, 170), size = (60, -1))
		self.button_refresh.SetBackgroundColour((255, 165, 0))
		self.button_refresh.Bind(wx.EVT_BUTTON, self.onRefresh)
		self.button_theme = wx.Button(self.panel, label = "Theme", pos = (203, 170), size = (60, -1))
		self.button_theme.SetBackgroundColour((0, 255, 255))
		self.button_theme.Bind(wx.EVT_BUTTON, self.onThemeChange)
		self.button_cancel = wx.Button(self.panel, label = "Close", pos = (285, 170), size = (60, -1))
		self.button_cancel.SetBackgroundColour((255, 0, 0))
		self.button_cancel.Bind(wx.EVT_BUTTON, self.onClose)
		self.isBlack = False
	
	def onCompute(self, event):
		if (self.compute_BMI(self.height.GetValue(), self.weight.GetValue()) == None):
			self.result_text.SetLabel("... kg/(m*m)")
		else:
			self.result_text.SetLabel(str(self.compute_BMI(self.height.GetValue(), self.weight.GetValue())) + " kg/(m*m)")
		self.button_compute.SetBackgroundColour((0, 0, 255))
		time.sleep(0.1)
		self.button_compute.SetBackgroundColour((0, 255, 0))
	
	def onRefresh(self, event):
		self.result_text.SetLabel("... kg/(m*m)")
		self.error_text.SetLabel("")
		self.height.SetValue(0)
		self.weight.SetValue(0)
		
	def onThemeChange(self, event):
		if (self.isBlack == False):
			self.panel.SetBackgroundColour("Black")
			self.info_text.SetForegroundColour((255, 255, 255))
			self.label_text.SetForegroundColour((255, 255, 255))
			self.result_text.SetForegroundColour((255, 255, 255))
			self.error_label.SetForegroundColour((255, 255, 255))
			self.error_text.SetForegroundColour((255, 255, 255))
			self.static_text_height.SetForegroundColour((255, 255, 255))
			self.static_text_height_extra.SetForegroundColour((255, 255, 255))
			self.static_text_weight.SetForegroundColour((255, 255, 255))
			self.static_text_weight_extra.SetForegroundColour((255, 255, 255))
			self.bmi_underweight.SetForegroundColour((255, 255, 255))
			self.bmi_normal_weight.SetForegroundColour((255, 255, 255))
			self.bmi_overweight.SetForegroundColour((255, 255, 255))
			self.bmi_obesity.SetForegroundColour((255, 255, 255))
			self.button_compute.SetForegroundColour((255, 255, 255))
			self.button_refresh.SetForegroundColour((255, 255, 255))
			self.button_theme.SetForegroundColour((255, 255, 255))
			self.button_cancel.SetForegroundColour((255, 255, 255))
			self.isBlack = True
		elif (self.isBlack == True):
			self.panel.SetBackgroundColour("White")
			self.info_text.SetForegroundColour((0, 0, 0))
			self.label_text.SetForegroundColour((0, 0, 0))
			self.result_text.SetForegroundColour((0, 0, 0))
			self.error_label.SetForegroundColour((0, 0, 0))
			self.error_text.SetForegroundColour((0, 0, 0))
			self.static_text_height.SetForegroundColour((0, 0, 0))
			self.static_text_height_extra.SetForegroundColour((0, 0, 0))
			self.static_text_weight.SetForegroundColour((0, 0, 0))
			self.static_text_weight_extra.SetForegroundColour((0, 0, 0))
			self.bmi_underweight.SetForegroundColour((0, 0, 0))
			self.bmi_normal_weight.SetForegroundColour((0, 0, 0))
			self.bmi_overweight.SetForegroundColour((0, 0, 0))
			self.bmi_obesity.SetForegroundColour((0, 0, 0))
			self.button_compute.SetForegroundColour((0, 0, 0))
			self.button_refresh.SetForegroundColour((0, 0, 0))
			self.button_theme.SetForegroundColour((0, 0, 0))
			self.button_cancel.SetForegroundColour((0, 0, 0))
			self.isBlack = False
		self.panel.Refresh()
		
	def onClose(self, event):
		self.Close(True)
		self.button_cancel.SetBackgroundColour((0, 0, 255))
		time.sleep(0.1)
		self.button_cancel.SetBackgroundColour((255, 0, 0))
	
	def errorZeroDivision(self):
		self.error_text.SetLabel("Division by zero")
	
	def compute_BMI(self, height, weight):
		self.error_text.SetLabel("")
		height_m = float(height) / 100
		if ((height_m * height_m) == 0):
			self.errorZeroDivision()
			return None
		BMI = weight / (height_m * height_m)
		return BMI
	
def main():
	app = wx.App()
	frame = BMICalculator(None, -1)
	frame.Show()
	app.MainLoop()
	
if __name__ == "__main__":
	main()