# A First Course in the Finite Element Method, 4th Edition
# Daryl L. Logan
# Example 5.8
# Units for this model are kips and inches

# Import 'FEModel3D' and 'Visualization' from 'PyNite'
from PyNite import FEModel3D
import Visualization

#创建新模型
frame = FEModel3D()

#定义节点
frame.AddNode('N1', 0, 0, 0)
frame.AddNode('N2', -100, 0, 0)
frame.AddNode('N3', 0, 0, -100)
frame.AddNode('N4', 0, -100, 0)

# 定义support
frame.DefineSupport('N2', True, True, True, True, True, True)
frame.DefineSupport('N3', True, True, True, True, True, True)
frame.DefineSupport('N4', True, True, True, True, True, True)

# Create members (这个例子中所有杆件性质相同)
J = 50
Iy = 100
Iz = 100
E = 30000
G = 10000
A = 10

frame.AddMember('M1', 'N2', 'N1', E, G, Iy, Iz, J, A)
frame.AddMember('M2', 'N3', 'N1', E, G, Iy, Iz, J, A)
frame.AddMember('M3', 'N4', 'N1', E, G, Iy, Iz, J, A)

#添加节点荷载
frame.AddNodeLoad('N1', 'FZ', 50)
frame.AddNodeLoad('N1', 'MY', -100)

#进行力学分析
frame.Analyze(check_statics=True)

#渲染变形
Visualization.RenderModel(frame, text_height=5, deformed_shape=False,moment=True,deformed_scale=100, render_loads=True)

# Print the node 1 displacements
print('Node 1 deformations:')
print('Calculated values: ', frame.GetNode('N1').DX, frame.GetNode('N1').DY, frame.GetNode('N1').DZ, frame.GetNode('N1').RX, frame.GetNode('N1').RY, frame.GetNode('N1').RZ)
print('Expected values: ', 7.098e-5, -0.014, -2.352e-3, -3.996e-3, 1.78e-5, -1.033e-4)
