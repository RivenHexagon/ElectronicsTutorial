
# Voltage Sources
## Voltage Sources in General
In the previous lecture we talked about the water pump as an equivalent for a voltage source but did not go into any details about it. It is now time to demystify electrical sources and to find out what they are. This will lay the gound work for future lectures and, more importantly, practical applications. But before we do that, let me exploit that water circulation equivalent for a little more.

### Counter Forces
Take a hand operated water pump for instance. It builds up pressure as long as I crank its handle. The harder I crank it, the more pressure I build up. And vice versa, the more pressure I want, the harder I have to turn. I will soon notice a counter force that puts a limit to my effords. (That limit is basically defined by my personal fitness level.) The counter force allways acts against me. If there was no counter force, I could create energy out of thin air! So if you drove a water wheel with my hand pump - like in our  first lecture's example - this counter force told you that you have to perform a certain amount of work. And that means spending energy - since we allways have to pay the piper! That is basically what the fundamental laws of thermodynamics state.

As a side note: in theory I don't have to spent energy just to building up pressure. Not until I move any water or even drive a water wheel with it. But the pump faces intrinsic friction losses, as does any electrical generator. Hence, this model is not so far from the thruth.

### Open Loop Voltage
<!-- Let us analyse what happens in the moment a water circuit is connected to a water pump. When the valve opens, the water will experience a relaxation and the pressure will slightly drop. You can imagin a standing crowd of people cramped together before the start of a demonstration. The crowd on the move is not as packed as the standing pulk of people. But let us assume the pump compensates for that. -->

Originally we were able to *Kirchhoff's Voltage Law* very nicely from a water model. The law states that the sum of all voltages in an (elctrical) circuit equals zero. Or put another way: The source voltage equals the sum of all (serial) voltage drops in the connected circuit. Applied to the circulation of water we can say: If we monitor the pressure at the pump and across the pipes, including any water wheel connected to them, we will be able to make this summation correctly in the same way at any time. 

#### Are we violating *Kirchhoff's Voltage Law (KVL)?*
But what about the **static case**, when the valves of the pump are closed or when the source is disconnected from the load? In that case we can at least make this statement: The pressure that builds up before any valves open for the water to flow, is equivalent to the voltage of any electrical source before its terminals are connected to a circuit. This is called the **Open Loop Voltage V<sub>o</sub>**. But what about the voltage or pressure drops of the circuit? It appears that the opposing pressure or voltage drops were missing - like there was a pump pressure or a source voltage only! Isn't there anything left to sum up to zero like *KVL* states? To anwer that, let us focus on voltages only for the moment.

#### Closed loops
Let us draw a voltage indicator in form of an arrow left to our source, from top to bottom. Let us name it **V<sub>s</sub>** for source voltage. And now we draw another indicator to the right of our source, from the top terminal to the bottom terminal or from plus to minus respectively. We name it **V<sub>o</sub>** for open loop voltage. At first glance **V<sub>o</sub>** looks like an exact duplicate of **V<sub>s</sub>**.

Remember Lecture 1 where we rearranged our arrows of source voltage and voltage drops? **V<sub>s</sub>** appeared to be parallel to the sum of the Voltage drops along the wires and across the load resistor. But after a deft rearrangement we figured that the source voltage is **opposing** the other voltages but is equal in magnitude! The same rule applies here. **V<sub>s</sub>** and **V<sub>o</sub>** are just **vectors** in an **one-dimensional** space that is curved back into itself - in form of a **closed loop**, called a **circuit**. So mathematically we get **V<sub>s</sub>** = **V<sub>o</sub>** what can be rearranged to **V<sub>s</sub>** - **V<sub>o</sub>** = 0. This demonstrates that *KVL* is not violated. You cound simply imagine the open terminals as an infinite high resistance.

#### Tighten the Grip
As always, I would like to take a more intuitive approach to completing this. Let's go back to our water circuit, which consists of a pump and a water wheel. Both are connected by two conduits. The water wheel sits so tightly in its housing, that no water can pass through unless it is turning. When the pump starts, water flows through the pipes and sets the water wheel in motion. Pressure drops occur along the pipes and accross the water wheel.

Now I grip the axle of the water wheel. The tighter I grip, the slower the water wheel becomes and the less water flows. As a consequence, the pressure drops in the conduits become smaller and smaller. But what happens to the pressure drop across the water wheel? Well *Kirchoff* gives the answer. If the pump maintains a constant pressure **p<sub>p</sub>**, the pressure drop **p<sub>w</sub>** at the wheel must increase as the pressure drop **p<sub>c</sub>** across the conduits goes down due to the reduced flow. Only then the equation p<sub>p</sub> = p<sub>c</sub> + p<sub>w</sub> holds true. When I stop the wheel, the flow stops and the pressure drop across the pipes vanishes. Thus the pressure drop across the wheel **converges** with the pressure ceated by the pump. Therefore the **open circuit** is nothing other than the **limit transition** from the **dynamic** to the **static** case!

### The Chain of Cause and Effect
Let us now take a look at the chain of cause and effect and see where this takes us. I will use the water circuit and the electricity circuit interchangeably and reverse the causality chain. Drops in pressure are either caused by friction in the pipes or by relaxation of the water as it passes trough the wheel. The water flow is caused by a pressure difference generated by the pump between its inlet and outlet connections. Further is the difference in pressure caused by the displacement of water molecules.

Let us now take a circuit consisting of a light bulb connected to a voltage source via two wires. Both the wires and the light bulb generate voltage drops caused by the current flowing through their ohmic resistances.
And the current flow is caused by the **difference in potential** generated by the voltage source.

Pay close attention to how we indicate the source voltage V<sub>s</sub>, the current I and the voltage drops V<sub>L</sub> in a circuit diagram. The arrow representing the source voltage points from the positive to the negative pole of the source - or from top to bottom. The current flows from plus to minus **through** the connected **circuit**. This means that the current flows from minus to plus **within** the voltage **source**. The arrow indicating the current flow is therefore pointing in the **opposite** direction to the **source** voltage. This is different from ohmic resistors, where the current arrow and the voltage arrow point in the same direction. And this is in accordance with *Kirchhoff's Voltage Law*, according to which the source and load voltages are directed in opposite directions.

### Separation of Charge
The only thing left in the causality chain of our electrical circuit is the propper equivalent for the displacement of the water molecules by the pump. In the pump/pressure model we can also identify a source as a place where the flow is directed against the pressure drop. We could almost imagine the water flowing uphill.

In a pumped storage hydro power station for instance, water is pumped uphill against the gravitational field. This way enectrical energy is converted to potential engery and stored. If electricity is needed, the water flows downhill and drives a turbine connected to an electrical generator. When we move the water uphill we spent energy. When we let it run downhill we gain it, since energy can neither be generated nor destroyed.

But how can all this be applied to electrons? Let's just say that we have moved the electrons uphill against a certain field. But which field would that be? You've probably already guessed correctly - it's the **electric field**! But where does it emerge from?


## Types of Sources
A **pump** can be designed in certain ways. Let's take a **hand-operated** pump for instance. It pumps water as long as I **turn** the **crank**. There is no **control** over **pressure** or **flow** of any kind. Of course flow rate and pressure **depend** on how **hard** I crank it. And that is just a **casual** for how much **power** I apply. But I do not keep track of one or the other.

I could design an **automated** pump though, that has **control** over the **pressure** and keeps it at a **constant** level - **regardless** of how much water I draw off. Or to put in another way: *the **pressure** is **independent** of the **flow**.* The more water I draw within a certain amount if time, the **harder** it becomes for the pump to *maintain* the **pressure**. Consequently, the more **mechanical power** the pump draws.

An alternative pump design would **monitor** the **flow** and keep it **constant** over time - **regardless** of how hard it is to force the water into the connected pipe. Or in other words: *the **flow** is **independent** of the **pressure**.* The thinner the pipes are, the higher the pressure must be and the harder it is for the pump to *maintain* the **flow**. Consequently, the more **mechanical power** the pump draws.

## Voltage and Current Sources
Can you already **make** the **connection**?

## Electrons in Wires
Electrons inside a wire are like dogs beeing dragged on a leash from tree to tree.
