package example_1

object Euler1 extends App {
  /*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
 */
  def divThree(i: Int) : Boolean = {
    (i%3 ==0)
  }
  def divFive(i: Int) : Boolean = {
    (i%5 ==0)
  }

  def sumMultiples(i: Int, sum: Int) : Int = {
    i match {
      case x if x > 999 => sum
      case x if divThree(x) => sumMultiples(i + 1, sum + i)
      case x if divFive(x) => sumMultiples(i + 1, sum + i)
      case _ => sumMultiples(i + 1, sum)
    }
  }
  println(sumMultiples(0, 0))
}
