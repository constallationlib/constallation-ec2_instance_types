from instance_type import InstanceType

r7i_large = InstanceType(
    instance_family="r7i",
    instance_size="large",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=2,
    architecture="x86_64",
    cores=2,
    valid_cores=[1, 2],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=3.2,
    memory_gb=16.0,
    storage_gb=None,
    storage_type=None,
    network_performance="Up to 12.5 Gigabit",
    instance_storage_gb=None,
    gpu=False,
    gpu_count=0,
    gpu_memory_gb=0,
    eni=3,
    ipv6_support=True
)

r7i_xlarge = InstanceType(
    instance_family="r7i",
    instance_size="xlarge",
    free_tier_eligible=False,
    bare_metal=False,
    hypervisor="Nitro",
    vcpus=4,
    architecture="x86_64",
    cores=4,
    valid_cores=[2, 4],
    threads_per_core=1,
    valid_threads_per_core=[1],
    sustained_clock_speed=3.2,
    memory_gb=32.0,
   ⬤