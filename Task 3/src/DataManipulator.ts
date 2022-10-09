import { ServerRespond } from './DataStreamer';

export interface Row {
  price_abc: number,
  price_def: number,
  ratio: number,
  timestamp: Date,
  upper_bound: number,
  lower_bound: number,
  trigger_alert: number | undefined,
}


export class DataManipulator {
  static generateRow(serverResponse: ServerRespond[]): Row {
    const priceABC = (serverResponse[0].top_ask.price + serverResponse[0].top_bid.price) / 2;
    const priceDEF = (serverResponse[1].top_ask.price + serverResponse[1].top_bid.price) / 2;
    const ratio = priceABC / priceDEF
    const upperBound = 1.05  // 5% positive deviation (constant value)
    const lowerBound = 0.95  // 5% negative deviation (constant value)

    return {
      price_abc: priceABC,
      price_def: priceDEF,
      ratio: ratio,
      timestamp: serverResponse[0].timestamp > serverResponse[1].timestamp ? serverResponse[0].timestamp : serverResponse[1].timestamp,
      upper_bound: upperBound,
      lower_bound: lowerBound,
      trigger_alert: (ratio > upperBound || ratio < lowerBound) ? ratio : undefined,
    }
  }
}
