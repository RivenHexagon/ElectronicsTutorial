
# Voltage Sources
In the previous lecture we have learned about voltage sources by an equivalent - the water pump - and kept it that way. It is now time to demystify electrical sources. This will lay the gound work for future lectures and, more importantly, practical applications. But before we do that, let me exploit that equivalent of water circulation for a little more.

### Counter Forces
A hand operated water pump for instance builds up pressure as long as I crank its handle. The harder I crank it, the more pressure I build up. And vice versa: the more pressure I want, the harder I have to turn. I will soon notice a counter force that puts a limit to my effords. That limit is basically defined by my personal fitness level. The counter force allways acts against me. Allways and in every kind of source. Otherwise I could create energy out of thin air! If you wanted to drive a water wheel with my hand pump - like in our prevous example - this counter force tells you that you have to perform a certain amount of work. And that means spending energy. We all have to pay the piper!

In theory I don't have to spent energy just to building up pressure. Not until I move any water or even drive a water wheel with it. But the pump faces intrinsic friction losses, as does any electrical generator. Hence, this model is not so far from the thruth.

### Open Loop Voltage
<!-- Let us analyse what happens in the moment a water circuit is connected to a water pump. When the valve opens, the water will experience a relaxation and the pressure will slightly drop. You can imagin a standing crowd of people cramped together before the start of a demonstration. The crowd on the move is not as packed as the standing pulk of people. But let us assume the pump compensates for that. -->

Originally we derived *Kirchhoff's Voltage Law* so nicely from a water model. The law states that the sum of all voltages in an (elctrical) circuit equals zero. Or put another way: The source voltage equals the sum of all (serial) voltage drops in the connected circuit. This law is still applicable to the circulation of water: If we monitor the pressure at the pump and across the pipes ,plus any water wheel connected to them, we will be able to make this summation correctly at any time. And in fact the same holds true for the electrical circuit. 

#### Are we violating *Kirchhoff's Voltage Law?*
But what about the **static case**, when the valves of the pump are closed or when the source is disconnected from the load? The pressure that builds up before any valves open for the water to flow, is equivalent to the voltage of any electrical source before its terminals are connected to a circuit. This is called the **Open Loop Voltage V<sub>0</sub>**. But it appears that the opposing pressure or voltage drops are missing, like there was a pump pressure or a source voltage only! Is there anything left to sum up to zero? To anwer that, let us focus on voltages only for the moment.

Like before, let us draw a voltage indicator in form of an arrow left to our source, from top to bottom. Let us name it **V<sub>s</sub>** for source voltage. And now we draw another indicator to the right of our source, from the top terminal to the bottom terminal or from plus to minus respectively. We name it **V<sub>0</sub>** for open loop voltage. On first glance **V<sub>0</sub>** looks like an exact duplicate of **V<sub>s</sub>**.

#### Closed loops
Remember last time, how we rearranged our arrows of source voltage and voltage drops? **V<sub>s</sub>** appeared to be parallel to the sum of the Voltage drops in the wires and the load resistor. But after a deft rearrangement we figured that the source is **opposing** the other voltages but is equal in magnitude! The same rule applies here. **V<sub>s</sub>** and **V<sub>0</sub>** are just **vectors** in an **one-dimensional** space that is curved back into itself - in form of a **closed loop**. Or in other words - a **circuit**. So mathematically we get **V<sub>s</sub>** = **V<sub>0</sub>** => **V<sub>s</sub>** - **V<sub>0</sub>** = 0 - quod erat demonstrandum!

#### Tighten the Grip
As always, I would like to take a more intuitive approach to completing this. Let's go back to our water circuit, which consists of a pump and a water wheel connected to the pump by two pipes. The water wheel sits so tightly in its housing that no water can pass through unless it is turning. When the pump is running, the water flows through the pipes and sets the water wheel in motion. Pressure drops occur along the pipes and on the water wheel.

Now I grip the axle of the water wheel. The tighter I grip, the slower the water wheel becomes and the less water flows. The pressure drop in the pipes becomes smaller and smaller. What happens to the pressure drop across the water wheel? Well *Kirchoff* gives the answer. If the pump maintains a constant pressure, the pressure at the wheel must increase as the pressure drop across the pipes goes down due to the reduced flow. When I stop the wheel, the flow stops and the pressure drop across the pipes vanishes. Thus the pressure drop across the wheel **converges** with the pressure ceated by the pump. The open circuit therefore corresponds to the **limit transition** from the dynamic to the static case!

### The Chain of Cause and Action
[...]

## Types of Sources
A **pump** can be designed in certain ways. Let's take a **hand-operated** pump for instance. It pumps water as long as I **turn** the **crank**. There is no **control** over **pressure** or **flow** of any kind. Of course flow rate and pressure **depend** on how **hard** I crank it. And that is just a **casual** for how much **power** I apply. But I do not keep track of one or the other.

I could design an **automated** pump though, that has **control** over the **pressure** and keeps it at a **constant** level - **regardless** of how much water I draw off. Or to put in another way: *the **pressure** is **independent** of the **flow**.* The more water I draw within a certain amount if time, the **harder** it becomes for the pump to *maintain* the **pressure**. Consequently, the more **mechanical power** the pump draws.

An alternative pump design would **monitor** the **flow** and keep it **constant** over time - **regardless** of how hard it is to force the water into the connected pipe. Or in other words: *the **flow** is **independent** of the **pressure**.* The thinner the pipes are, the higher the pressure must be and the harder it is for the pump to *maintain* the **flow**. Consequently, the more **mechanical power** the pump draws.

## Voltage and Current Sources
Can you already **make** the **connection**?

## Electrons in Wires
Electrons inside a wire are like dogs beeing dragged on a leash from tree to tree.
