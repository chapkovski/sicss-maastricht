<template>
  <div id="app">
  <h6>Choose Participant A decision:</h6>
    <div class="slider-wrapper">
      <Slider
        sliderMin="0"
        :sliderMax="endowment"
        :sliderInt="1"
        @change-slider="senderval=$event;receiverval=0; initialRecVal=0"
      />
    </div>
    <h6>Choose Participant B decision:</h6>
    <div class="slider-wrapper" v-if="senderval !=='null'">
      <Slider
        sliderMin="0"
        :initialVal="initialRecVal"
        :sliderMax="multiplied_amount"
        :sliderInt="coef"
        @change-slider="receiverval=$event"
      />
    </div>

    <hr>

    <div class="my-3">Multiplied amount: {{multiplied_amount}}</div>

    <div
      class="my-3"
    >Sender payoff: {{endowment}} - {{senderval}} + {{receiverval}} =<b> {{sender_payoff}} points</b></div>
    <div
      class="my-3"
    >Receiver payoff: {{endowment}} + {{multiplied_amount}} - {{receiverval}} =<b> {{receiver_payoff}} points</b></div>
  </div>
</template>

<script>
import Slider from "./components/Slider";

export default {
  name: "App",
  components: {
    Slider
  },
  computed: {
    multiplied_amount() {
      return this.coef * this.senderval;
    },
    sender_payoff() {
      return this.endowment - this.senderval + this.receiverval;
    },
    receiver_payoff() {
      return this.endowment + this.multiplied_amount - this.receiverval;
    }
  },
  data() {
    return {
      endowment: 10,
      coef: 3,
      senderval: 0,
      receiverval: 0,
      initialRecVal: 0
    };
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.slider-wrapper {
  margin-bottom: 30px;
}
</style>
