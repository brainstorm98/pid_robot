#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robot_control_final.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import math
import threading
class Ui_MainWindow(object):

    def __init__(self):
        rospy.init_node("robot_arayuz")
        self.pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
        self.hiz_mesaji = Twist()
        self.sub = rospy.Subscriber("odom", Odometry, self.odomCallback)
        self.sub_2 = rospy.Subscriber("odom", Odometry, self.getRotation)
        self.isRunning = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 532)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.etiket_acisal_hiz_kontrolcu = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_acisal_hiz_kontrolcu.setFont(font)
        self.etiket_acisal_hiz_kontrolcu.setAlignment(QtCore.Qt.AlignCenter)
        self.etiket_acisal_hiz_kontrolcu.setObjectName("etiket_acisal_hiz_kontrolcu")
        self.gridLayout_2.addWidget(self.etiket_acisal_hiz_kontrolcu, 0, 0, 1, 1)
        self.etiket_lineer_hiz_kontrolcu = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_lineer_hiz_kontrolcu.setFont(font)
        self.etiket_lineer_hiz_kontrolcu.setAlignment(QtCore.Qt.AlignCenter)
        self.etiket_lineer_hiz_kontrolcu.setObjectName("etiket_lineer_hiz_kontrolcu")
        self.gridLayout_2.addWidget(self.etiket_lineer_hiz_kontrolcu, 0, 1, 1, 1)
        self.etiket_otonom_robot = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_otonom_robot.setFont(font)
        self.etiket_otonom_robot.setAlignment(QtCore.Qt.AlignCenter)
        self.etiket_otonom_robot.setObjectName("etiket_otonom_robot")
        self.gridLayout_2.addWidget(self.etiket_otonom_robot, 5, 2, 1, 1)
        self.etiket_hedeflenen_konum_gostergesi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_hedeflenen_konum_gostergesi.setFont(font)
        self.etiket_hedeflenen_konum_gostergesi.setAlignment(QtCore.Qt.AlignCenter)
        self.etiket_hedeflenen_konum_gostergesi.setObjectName("etiket_hedeflenen_konum_gostergesi")
        self.gridLayout_2.addWidget(self.etiket_hedeflenen_konum_gostergesi, 2, 0, 1, 2)
        self.etiket_anlik_konum_gostergesi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_anlik_konum_gostergesi.setFont(font)
        self.etiket_anlik_konum_gostergesi.setAlignment(QtCore.Qt.AlignCenter)
        self.etiket_anlik_konum_gostergesi.setObjectName("etiket_anlik_konum_gostergesi")
        self.gridLayout_2.addWidget(self.etiket_anlik_konum_gostergesi, 2, 2, 1, 1)
        self.hedeflenen_konum_layout = QtWidgets.QGridLayout()
        self.hedeflenen_konum_layout.setObjectName("hedeflenen_konum_layout")
        self.etiket_hedeflenen_konum_x = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.etiket_hedeflenen_konum_x.setFont(font)
        self.etiket_hedeflenen_konum_x.setObjectName("etiket_hedeflenen_konum_x")
        self.hedeflenen_konum_layout.addWidget(self.etiket_hedeflenen_konum_x, 0, 0, 1, 1)
        self.etiket_hedeflenen_konum_y = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.etiket_hedeflenen_konum_y.setFont(font)
        self.etiket_hedeflenen_konum_y.setObjectName("etiket_hedeflenen_konum_y")
        self.hedeflenen_konum_layout.addWidget(self.etiket_hedeflenen_konum_y, 1, 0, 1, 1)
        self.line_hedeflenen_konum_x = QtWidgets.QLineEdit(self.centralwidget)
        self.line_hedeflenen_konum_x.setObjectName("line_hedeflenen_konum_x")
        self.hedeflenen_konum_layout.addWidget(self.line_hedeflenen_konum_x, 0, 1, 1, 1)
        self.line_hedeflenen_konum_y = QtWidgets.QLineEdit(self.centralwidget)
        self.line_hedeflenen_konum_y.setObjectName("line_hedeflenen_konum_y")
        self.hedeflenen_konum_layout.addWidget(self.line_hedeflenen_konum_y, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.hedeflenen_konum_layout, 3, 0, 1, 2)
        self.anlik_hiz_layout = QtWidgets.QGridLayout()
        self.anlik_hiz_layout.setObjectName("anlik_hiz_layout")
        self.etiket_anlik_lineer_hiz = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.etiket_anlik_lineer_hiz.setFont(font)
        self.etiket_anlik_lineer_hiz.setObjectName("etiket_anlik_lineer_hiz")
        self.anlik_hiz_layout.addWidget(self.etiket_anlik_lineer_hiz, 0, 0, 1, 1)
        self.line_anlik_lineer_hiz = QtWidgets.QLineEdit(self.centralwidget)
        self.line_anlik_lineer_hiz.setReadOnly(True)
        self.line_anlik_lineer_hiz.setObjectName("line_anlik_lineer_hiz")
        self.anlik_hiz_layout.addWidget(self.line_anlik_lineer_hiz, 0, 1, 1, 1)
        self.etiket_anlik_acisal_hiz = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.etiket_anlik_acisal_hiz.setFont(font)
        self.etiket_anlik_acisal_hiz.setObjectName("etiket_anlik_acisal_hiz")
        self.anlik_hiz_layout.addWidget(self.etiket_anlik_acisal_hiz, 1, 0, 1, 1)
        self.line_anlik_acisal_hiz = QtWidgets.QLineEdit(self.centralwidget)
        self.line_anlik_acisal_hiz.setReadOnly(True)
        self.line_anlik_acisal_hiz.setObjectName("line_anlik_acisal_hiz")
        self.anlik_hiz_layout.addWidget(self.line_anlik_acisal_hiz, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.anlik_hiz_layout, 1, 2, 1, 1)
        self.etiket_anlik_hiz_gostergesi = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.etiket_anlik_hiz_gostergesi.setFont(font)
        self.etiket_anlik_hiz_gostergesi.setAlignment(QtCore.Qt.AlignCenter)
        self.etiket_anlik_hiz_gostergesi.setObjectName("etiket_anlik_hiz_gostergesi")
        self.gridLayout_2.addWidget(self.etiket_anlik_hiz_gostergesi, 0, 2, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.etiket_Kp_acisal = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.etiket_Kp_acisal.setFont(font)
        self.etiket_Kp_acisal.setObjectName("etiket_Kp_acisal")
        self.gridLayout_5.addWidget(self.etiket_Kp_acisal, 0, 0, 1, 1)
        self.line_Kp_acisal = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Kp_acisal.setObjectName("line_Kp_acisal")
        self.gridLayout_5.addWidget(self.line_Kp_acisal, 0, 1, 1, 1)
        self.etiket_Ki_acisal = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.etiket_Ki_acisal.setFont(font)
        self.etiket_Ki_acisal.setObjectName("etiket_Ki_acisal")
        self.gridLayout_5.addWidget(self.etiket_Ki_acisal, 1, 0, 1, 1)
        self.line_Ki_acisal = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Ki_acisal.setObjectName("line_Ki_acisal")
        self.gridLayout_5.addWidget(self.line_Ki_acisal, 1, 1, 1, 1)
        self.etiket_Kd_acisal = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.etiket_Kd_acisal.setFont(font)
        self.etiket_Kd_acisal.setObjectName("etiket_Kd_acisal")
        self.gridLayout_5.addWidget(self.etiket_Kd_acisal, 2, 0, 1, 1)
        self.line_Kd_acisal = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Kd_acisal.setObjectName("line_Kd_acisal")
        self.gridLayout_5.addWidget(self.line_Kd_acisal, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.robot_kontrol_layout = QtWidgets.QGridLayout()
        self.robot_kontrol_layout.setObjectName("robot_kontrol_layout")
        self.buton_dur = QtWidgets.QPushButton(self.centralwidget)
        self.buton_dur.setObjectName("buton_dur")
        self.robot_kontrol_layout.addWidget(self.buton_dur, 1, 1, 1, 1)
        self.buton_ileri = QtWidgets.QPushButton(self.centralwidget)
        self.buton_ileri.setObjectName("buton_ileri")
        self.robot_kontrol_layout.addWidget(self.buton_ileri, 0, 1, 1, 1)
        self.buton_sol = QtWidgets.QPushButton(self.centralwidget)
        self.buton_sol.setObjectName("buton_sol")
        self.robot_kontrol_layout.addWidget(self.buton_sol, 1, 0, 1, 1)
        self.buton_geri = QtWidgets.QPushButton(self.centralwidget)
        self.buton_geri.setObjectName("buton_geri")
        self.robot_kontrol_layout.addWidget(self.buton_geri, 2, 1, 1, 1)
        self.buton_sag = QtWidgets.QPushButton(self.centralwidget)
        self.buton_sag.setObjectName("buton_sag")
        self.robot_kontrol_layout.addWidget(self.buton_sag, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.robot_kontrol_layout, 6, 0, 1, 2)
        self.etiket_manuel_robot = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.etiket_manuel_robot.setFont(font)
        self.etiket_manuel_robot.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.etiket_manuel_robot.setAlignment(QtCore.Qt.AlignCenter)
        self.etiket_manuel_robot.setObjectName("etiket_manuel_robot")
        self.gridLayout_2.addWidget(self.etiket_manuel_robot, 5, 0, 1, 2)
        self.anlik_konum_layout = QtWidgets.QGridLayout()
        self.anlik_konum_layout.setObjectName("anlik_konum_layout")
        self.etiket_anlik_konum_x = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.etiket_anlik_konum_x.setFont(font)
        self.etiket_anlik_konum_x.setObjectName("etiket_anlik_konum_x")
        self.anlik_konum_layout.addWidget(self.etiket_anlik_konum_x, 0, 0, 1, 1)
        self.line_anlik_konum_x = QtWidgets.QLineEdit(self.centralwidget)
        self.line_anlik_konum_x.setReadOnly(True)
        self.line_anlik_konum_x.setObjectName("line_anlik_konum_x")
        self.anlik_konum_layout.addWidget(self.line_anlik_konum_x, 0, 1, 1, 1)
        self.etiket_anlik_konum_y = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.etiket_anlik_konum_y.setFont(font)
        self.etiket_anlik_konum_y.setObjectName("etiket_anlik_konum_y")
        self.anlik_konum_layout.addWidget(self.etiket_anlik_konum_y, 1, 0, 1, 1)
        self.line_anlik_konum_y = QtWidgets.QLineEdit(self.centralwidget)
        self.line_anlik_konum_y.setReadOnly(True)
        self.line_anlik_konum_y.setObjectName("line_anlik_konum_y")
        self.anlik_konum_layout.addWidget(self.line_anlik_konum_y, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.anlik_konum_layout, 3, 2, 1, 1)
        self.otonom_robot_kontrol_layout = QtWidgets.QGridLayout()
        self.otonom_robot_kontrol_layout.setObjectName("otonom_robot_kontrol_layout")
        self.buton_otonom_start = QtWidgets.QPushButton(self.centralwidget)
        self.buton_otonom_start.setObjectName("buton_otonom_start")
        self.otonom_robot_kontrol_layout.addWidget(self.buton_otonom_start, 0, 0, 1, 1)
        self.buton_otonom_stop = QtWidgets.QPushButton(self.centralwidget)
        self.buton_otonom_stop.setObjectName("buton_otonom_stop")
        self.otonom_robot_kontrol_layout.addWidget(self.buton_otonom_stop, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.otonom_robot_kontrol_layout, 6, 2, 1, 1)
        self.lineer_hiz_layout = QtWidgets.QGridLayout()
        self.lineer_hiz_layout.setObjectName("lineer_hiz_layout")
        self.etiket_Kd_lineer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.etiket_Kd_lineer.setFont(font)
        self.etiket_Kd_lineer.setObjectName("etiket_Kd_lineer")
        self.lineer_hiz_layout.addWidget(self.etiket_Kd_lineer, 2, 0, 1, 1)
        self.etiket_Kp_lineer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.etiket_Kp_lineer.setFont(font)
        self.etiket_Kp_lineer.setObjectName("etiket_Kp_lineer")
        self.lineer_hiz_layout.addWidget(self.etiket_Kp_lineer, 0, 0, 1, 1)
        self.etiket_Ki_lineer = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.etiket_Ki_lineer.setFont(font)
        self.etiket_Ki_lineer.setObjectName("etiket_Ki_lineer")
        self.lineer_hiz_layout.addWidget(self.etiket_Ki_lineer, 1, 0, 1, 1)
        self.line_Kp_lineer = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Kp_lineer.setObjectName("line_Kp_lineer")
        self.lineer_hiz_layout.addWidget(self.line_Kp_lineer, 0, 1, 1, 1)
        self.line_Ki_lineer = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Ki_lineer.setObjectName("line_Ki_lineer")
        self.lineer_hiz_layout.addWidget(self.line_Ki_lineer, 1, 1, 1, 1)
        self.line_Kd_lineer = QtWidgets.QLineEdit(self.centralwidget)
        self.line_Kd_lineer.setObjectName("line_Kd_lineer")
        self.lineer_hiz_layout.addWidget(self.line_Kd_lineer, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.lineer_hiz_layout, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot Control Interface"))
        self.etiket_acisal_hiz_kontrolcu.setText(_translate("MainWindow", "Angular Velocity Controller Parameters"))
        self.etiket_lineer_hiz_kontrolcu.setText(_translate("MainWindow", "Linear Velocity Controller Parameters"))
        self.etiket_otonom_robot.setText(_translate("MainWindow", "Autonomous Robot Control"))
        self.etiket_hedeflenen_konum_gostergesi.setText(_translate("MainWindow", "Target Position Parameters"))
        self.etiket_anlik_konum_gostergesi.setText(_translate("MainWindow", "Current Position Display"))
        self.etiket_hedeflenen_konum_x.setText(_translate("MainWindow", "Target Position X (m):"))
        self.etiket_hedeflenen_konum_y.setText(_translate("MainWindow", "Target Position Y (m):"))
        self.etiket_anlik_lineer_hiz.setText(_translate("MainWindow", "Linear Velocity (m/s):"))
        self.etiket_anlik_acisal_hiz.setText(_translate("MainWindow", "Angular Velocity (rad/s):"))
        self.etiket_anlik_hiz_gostergesi.setText(_translate("MainWindow", "Current Velocity Display"))
        self.etiket_Kp_acisal.setText(_translate("MainWindow", "Kp_angular:"))
        self.etiket_Ki_acisal.setText(_translate("MainWindow", "Ki_angular:"))
        self.etiket_Kd_acisal.setText(_translate("MainWindow", "Kd_angular:"))
        self.buton_dur.setText(_translate("MainWindow", "Stop"))
        self.buton_ileri.setText(_translate("MainWindow", "Forward"))
        self.buton_sol.setText(_translate("MainWindow", "Left"))
        self.buton_geri.setText(_translate("MainWindow", "Backward"))
        self.buton_sag.setText(_translate("MainWindow", "Right"))
        self.etiket_manuel_robot.setText(_translate("MainWindow", "Manual Robot Control"))
        self.etiket_anlik_konum_x.setText(_translate("MainWindow", "Current Position X (m):"))
        self.etiket_anlik_konum_y.setText(_translate("MainWindow", "Current Position Y (m):"))
        self.buton_otonom_start.setText(_translate("MainWindow", "Start Autonomous Driving"))
        self.buton_otonom_stop.setText(_translate("MainWindow", "Stop Autonomous Driving"))
        self.etiket_Kd_lineer.setText(_translate("MainWindow", "Kd_linear:"))
        self.etiket_Kp_lineer.setText(_translate("MainWindow", "Kp_linear:"))
        self.etiket_Ki_lineer.setText(_translate("MainWindow", "Ki_linear:"))

        self.buton_dur.clicked.connect(self.robotDur)
        self.buton_ileri.clicked.connect(self.ileriGit)
        self.buton_geri.clicked.connect(self.geriGit)
        self.buton_sol.clicked.connect(self.solaDon)
        self.buton_sag.clicked.connect(self.sagaDon)
        self.buton_otonom_start.clicked.connect(self.start_otonom_thread)
        self.buton_otonom_stop.clicked.connect(self.otonomsurusDur)
        self.otonom_thread = None

        self.Kp_acisal = 0.05
        self.Ki_acisal = 0.0000005
        self.Kd_acisal = 2
        self.Kp_lineer = 0.1
        self.Ki_lineer = 0.0000005
        self.Kd_lineer = 2
        self.hedef_x = 0.0
        self.hedef_y = 0.0
        self.yaw = 0.0

        self.line_anlik_acisal_hiz.setText(str(0.0))
        self.line_anlik_lineer_hiz.setText(str(0.0))
        self.line_Kp_acisal.setText(str(self.Kp_acisal))
        self.line_Ki_acisal.setText('{:.7f}'.format(self.Ki_acisal))
        self.line_Kd_acisal.setText(str(self.Kd_acisal))
        self.line_Kp_lineer.setText(str(self.Kp_lineer))
        self.line_Ki_lineer.setText('{:.7f}'.format(self.Ki_lineer))
        self.line_Kd_lineer.setText(str(self.Kd_lineer))
        self.line_hedeflenen_konum_x.setText(str(self.hedef_x))
        self.line_hedeflenen_konum_y.setText(str(self.hedef_y))

    def odomCallback(self, mesaj):
        self.x = mesaj.pose.pose.position.x
        self.y = mesaj.pose.pose.position.y
        self.line_anlik_konum_x.setText(str(round(self.x, 2)))
        self.line_anlik_konum_y.setText(str(round(self.y, 2)))

    def getRotation(self, mesaj):
        orientation_q = mesaj.pose.pose.orientation
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (self.roll, self.pitch, self.yaw) = euler_from_quaternion(orientation_list)

    def robotDur(self):
        self.hiz_mesaji.linear.x = 0.0
        self.hiz_mesaji.angular.z = 0.0
        self.pub.publish(self.hiz_mesaji)
        self.line_anlik_lineer_hiz.setText(str(self.hiz_mesaji.linear.x))
        self.line_anlik_acisal_hiz.setText(str(self.hiz_mesaji.angular.z))

    def ileriGit(self):
        self.hiz_mesaji.linear.x = 1.0
        self.hiz_mesaji.angular.z = 0.0
        self.pub.publish(self.hiz_mesaji)
        self.line_anlik_lineer_hiz.setText(str(self.hiz_mesaji.linear.x))
        self.line_anlik_acisal_hiz.setText(str(self.hiz_mesaji.angular.z))

    def geriGit(self):
        self.hiz_mesaji.linear.x = -1.0
        self.hiz_mesaji.angular.z = 0.0
        self.pub.publish(self.hiz_mesaji)
        self.line_anlik_lineer_hiz.setText(str(self.hiz_mesaji.linear.x))
        self.line_anlik_acisal_hiz.setText(str(self.hiz_mesaji.angular.z))

    def solaDon(self):
        self.hiz_mesaji.linear.x = 1.0
        self.hiz_mesaji.angular.z = 0.5
        self.pub.publish(self.hiz_mesaji)
        self.line_anlik_lineer_hiz.setText(str(self.hiz_mesaji.linear.x))
        self.line_anlik_acisal_hiz.setText(str(self.hiz_mesaji.angular.z))

    def sagaDon(self):
        self.hiz_mesaji.linear.x = 1.0
        self.hiz_mesaji.angular.z = -0.5
        self.pub.publish(self.hiz_mesaji)
        self.line_anlik_lineer_hiz.setText(str(self.hiz_mesaji.linear.x))
        self.line_anlik_acisal_hiz.setText(str(self.hiz_mesaji.angular.z))

    def get_Kp_Acisal(self):
        kp_text_acisal = self.line_Kp_acisal.text()
        if kp_text_acisal.replace('.', '', 1).isdigit():
            self.Kp_acisal = float(kp_text_acisal)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, 'Error', 'Invalid angular Kp value. Please enter a valid number.')
            self.Kp_Acisal = 0.05
            self.line_Kp_acisal.setText(str(self.Kp_acisal))
    def get_Ki_Acisal(self):
        ki_text_acisal = self.line_Ki_acisal.text()
        if ki_text_acisal.replace('.', '', 1).isdigit():
            self.Ki_acisal = float(ki_text_acisal)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, 'Error', 'Invalid angular Ki value. Please enter a valid number.')

    def get_Kd_Acisal(self):
        kd_text_acisal = self.line_Kd_acisal.text()
        if kd_text_acisal.replace('.', '', 1).isdigit():
            self.Kd_acisal = float(kd_text_acisal)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, 'Error', 'Invalid angular Kd value. Please enter a valid number.')

    def get_Kp_Lineer(self):
        kp_text_lineer = self.line_Kp_lineer.text()
        if kp_text_lineer.replace('.', '', 1).isdigit():
            self.Kp_lineer = float(kp_text_lineer)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, 'Error', 'Invalid linear Kp value. Please enter a valid number.')

    def get_Kd_Lineer(self):
        kd_text_lineer = self.line_Kd_lineer.text()
        if kd_text_lineer.replace('.', '', 1).isdigit():
            self.Kd_lineer = float(kd_text_lineer)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, 'Error', 'Invalid linear Kd value. Please enter a valid number.')

    def get_Ki_Lineer(self):
        ki_text_lineer = self.line_Ki_lineer.text()
        if ki_text_lineer.replace('.', '', 1).isdigit():
            self.Ki_lineer = float(ki_text_lineer)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, 'Error', 'Invalid linear Ki value. Please enter a valid number.')

    def hedef_konumX(self):
        line_hedeflenen_konum_x_text = self.line_hedeflenen_konum_x.text()
        if line_hedeflenen_konum_x_text.replace('.', '', 1).isdigit():
            self.hedef_x = float(line_hedeflenen_konum_x_text)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, 'Error', 'Invalid target position value. Please enter a number.')

    def hedef_konumY(self):
        line_hedeflenen_konum_y_text = self.line_hedeflenen_konum_y.text()
        if line_hedeflenen_konum_y_text.replace('.', '', 1).isdigit():
            self.hedef_y = float(line_hedeflenen_konum_y_text)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, 'Error', 'Invalid target position value. Please enter a number.')

        
    def autonomousdrivingStart(self):

        self.Kp_lineer = float(self.line_Kp_lineer.text())
        self.Kp_acisal = float(self.line_Kp_acisal.text())
        self.Ki_lineer = float(self.line_Ki_lineer.text())
        self.Ki_acisal = float(self.line_Ki_acisal.text())
        self.Kd_lineer = float(self.line_Kd_lineer.text())
        self.Kd_acisal = float(self.line_Kd_acisal.text())
        self.hedef_x = float(self.line_hedeflenen_konum_x.text())
        self.hedef_y = float(self.line_hedeflenen_konum_y.text())
        self.line_Kp_acisal.setReadOnly(True)
        self.line_Ki_acisal.setReadOnly(True)
        self.line_Kd_acisal.setReadOnly(True)
        self.line_Kp_lineer.setReadOnly(True)
        self.line_Ki_lineer.setReadOnly(True)
        self.line_Kd_lineer.setReadOnly(True)
        self.line_hedeflenen_konum_x.setReadOnly(True)
        self.line_hedeflenen_konum_y.setReadOnly(True)

        error_angular_old = 0.0
        error_lineer_old = 0.0
        integral_lineer_error = 0.0
        integral_angular_error = 0.0
        self.isRunning = True
        while not rospy.is_shutdown() and self.isRunning:
            loop_rate = rospy.Rate(10)
            velocity_error = math.sqrt((self.hedef_x - self.x) ** 2 + (self.hedef_y - self.y) ** 2)
            if velocity_error > 0.05:
                lineer_velocity_correction = self.Kp_lineer * velocity_error
                integral_lineer_error += velocity_error
                lineer_velocity_correction += self.Ki_lineer * integral_lineer_error
                lineer_velocity_correction -= self.Kd_lineer * (velocity_error - error_lineer_old)
                error_lineer_old = velocity_error
            else:
                lineer_velocity_correction = 0.0
            target_angle = math.atan2(self.hedef_y - self.y, self.hedef_x - self.x)
            angular_error = target_angle - self.yaw
            angular_velocity_correction = self.Kp_acisal * angular_error
            integral_angular_error = integral_angular_error + angular_error
            angular_velocity_correction = angular_velocity_correction + self.Ki_acisal * integral_angular_error
            angular_velocity_correction = angular_velocity_correction - (self.Kd_acisal * (angular_error - error_angular_old))
            error_angular_old = angular_error
            max_angular_correction = 0.3
            if abs(angular_error) > max_angular_correction:
                angular_velocity_correction = max_angular_correction
            elif angular_error < -max_angular_correction:
                angular_velocity_correction = -max_angular_correction
            else:
                angular_velocity_correction = angular_error * self.Ki_acisal
            self.hiz_mesaji.linear.x = lineer_velocity_correction
            self.hiz_mesaji.angular.z = angular_velocity_correction
            self.pub.publish(self.hiz_mesaji)
            if abs(velocity_error) < 0.05:
                self.hiz_mesaji.linear.x = 0.0
                self.hiz_mesaji.angular.z = 0.0
                self.pub.publish(self.hiz_mesaji)
                break
            loop_rate.sleep()
          
    def start_otonom_thread(self):
        if self.otonom_thread and self.otonom_thread.is_alive():
            return
        self.get_Kp_Acisal()
        self.get_Kd_Acisal()
        self.get_Ki_Acisal()
        self.get_Kp_Lineer()
        self.get_Kd_Lineer()
        self.get_Ki_Lineer()
        self.hedef_konumX()
        self.hedef_konumY()
        self.otonom_thread = threading.Thread(target=self.autonomousdrivingStart)
        self.otonom_thread.start()

    def otonomsurusDur(self):
        self.line_Kp_acisal.setReadOnly(False)
        self.line_Ki_acisal.setReadOnly(False)
        self.line_Kd_acisal.setReadOnly(False)
        self.line_Kp_lineer.setReadOnly(False)
        self.line_Ki_lineer.setReadOnly(False)
        self.line_Kd_lineer.setReadOnly(False)
        self.line_hedeflenen_konum_x.setReadOnly(False)
        self.line_hedeflenen_konum_y.setReadOnly(False)
        self.isRunning = False
        self.hiz_mesaji.linear.x = 0.0
        self.hiz_mesaji.angular.z = 0.0
        self.pub.publish(self.hiz_mesaji)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.isUIRunning = True
    MainWindow.show()
    ui.isUIRunning = False
    sys.exit(app.exec_())
