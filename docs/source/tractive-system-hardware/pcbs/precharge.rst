Pre-Charge Circuit
==================

Description
###########
The purpose of the Pre-Charge Circuit is to prevent a high inrush current when
opening the AIRs. High inrush current would happen without the Pre-Charge
circuit as the low initial resistance of the inverter causes an effective
shortcut, which risks overloading components in the tractive system. The
Pre-Charge Circuit is designed to limit inrush current by using a relay to
redirect the current through a resistor. The potential difference
accross the resistor is required to reach 95% of the maximum
Tractive System voltage before the Pre-Charge relay, and second AIR, may be
close. Relevant rules are EV 5.7 of the `FSG Rules
<https://www.formulastudent.de/fileadmin/user_upload/all/2020/rules/FS-Rules_2020_V1.0.pdf>`_.

Resources
#########
* `Michael Ruppe Pre-Charge Website <https://michaelruppe.com/2020/10/09/a-plug-n-play-precharger-fsae-electric/>`_: Has a useful description of how the Pre-Charge Circuit works
* `Michael Ruppe Pre-Charge Schematic <https://github.com/michaelruppe/FSAE/blob/master/Precharge/docs/schematic-v1.1.pdf>`_: An example circuit diagram of the Pre-Charge Circuit
* `craiguk62 Pre-Charge Explanation <https://www.youtube.com/watch?v=L6z1lT_QTXM>`_: Very useful video by and FSUK Judge explaining how the Pre-Charge Circuit works and explaing the rules around it
* `How to Design a Precharge Circuit <https://www.sensata.com/sites/default/files/a/sensata-how-to-design-precharge-circuits-evs-whitepaper.pdf>`_: Useful walkthrough of designing a Precharge circuit by Sensata
