Discharge Circuit
=================

Priority: **critical**

Description
###########

When the accumulator is disconnected, this circuit ensures the vehicle is in a safe state by discharging any energy stored in the TS across a high-power resistor. 

* The TS is considered discharged if its voltage is below 60V. (what rule?)
* The circuit must be able to discharge the full accumulator voltage (580V) three times within 15 seconds. (EV 4.9.1)
* The circuit must be fail-safe. It must discharge even if the HVD has been opened or the accumulator is disconnected. (EV 4.9.2)
* Fusing of the discharge main current path is prohibited. (EV 4.9.3)

**Resources**
#############

* `craiguk62 Discharge Explanation <https://www.youtube.com/watch?v=L6z1lT_QTXM>`_: Very useful video by FSUK Judge.
